import os
from collections import defaultdict
from enum import Enum, auto, IntEnum
from objects import Schema, Table, Column, Index, IndexColumn, IndexUsage

import pyodbc


class Reason(Enum):
    EXACT = auto()
    OVERLAPPING_INCLUDES = auto()
    DIFFERENT_INCLUDES = auto()
    OVERLAP = auto()
    ALMOST = auto()
    INCLUDE = auto()
    UNIQUE = auto()


def connect_objects(schemas, tables, columns, indexes, index_columns, index_usage):
    """
    Connect the objects to each other. Tables are in a Schema and have Columns and Indexes which also have Columns etc.
    """
    for schema in schemas.values():
        for table in tables.values():
            if table.schema_id == schema.schema_id:
                schema.tables.add(table)
                table.schema = schema

    for table in tables.values():
        for column in columns.values():
            if column.object_id == table.object_id:
                table.columns.append(column)
                column.table = table

    for index in indexes.values():
        if index.object_id in tables:
            index.table = tables[index.object_id]
            tables[index.object_id].indexes.add(index)

    for index_column in index_columns.values():
        index_column.name = columns[(index_column.object_id, index_column.column_id)].name
        if (index_column.object_id, index_column.index_id) in indexes:
            if index_column.is_included_column:
                indexes[(index_column.object_id, index_column.index_id)].includes.add(index_column)
            else:
                indexes[(index_column.object_id, index_column.index_id)].columns.append(index_column)

    for ix_usage in index_usage.values():
        if (ix_usage.object_id, ix_usage.index_id) in indexes:
            indexes[(ix_usage.object_id, ix_usage.index_id)].usage = ix_usage

    return schemas, tables, columns, indexes, index_columns, index_usage


class DuplicateIndex:
    """
    This class holds a Table and two indexes that are, somehow, duplicates or each other.
    The exact reason why they are duplicates is not past of this class.
    Classes of t1(c1, c2) equal t1(c2, c1) so we override __eq__ and __hash__.
    """
    def __init__(self, table: Table, index1: Index, index2: Index):
        self.table = table
        self.index1 = index1
        self.index2 = index2

    def __str__(self):
        return f"{self.table}: {self.index1} <--> {self.index2}"

    def __eq__(self, other: "DuplicateIndex"):
        if self.table != other.table:
            return False
        if self.index1 == other.index1 and self.index2 == other.index2:
            return True
        if self.index2 == other.index1 and self.index1 == other.index2:
            return True
        return False

    def __hash__(self):
        return hash((self.table.object_id, min(self.index1.index_id, self.index2.index_id), max(self.index1.index_id, self.index2.index_id)))


def inspect(tables):
    doubles: dict[DuplicateIndex, Reason] = {}
    for table in tables.values():
        this: Index
        that: Index
        for this in table.indexes:
            for that in table.indexes:
                if this == that:
                    continue

                #   UNIQUE will detect indexes that should be unique but are not
                #   unique t1(c1) vs t1(c1, c2) -> t1(c1, c2) should be unique also
                #   we don't continue after we find this case because it may have other issues as well
                if not this.is_unique and not this.is_unique_constraint:
                    if that.is_unique or that.is_unique_constraint:
                        if set(c.column_id for c in that.columns).issubset(set(c.column_id for c in this.columns)):
                            doubles[DuplicateIndex(table, this, that)] = Reason.UNIQUE

                if DuplicateIndex(table, this, that) in doubles:
                    # calls DuplicateIndex.__hash__ then, if false, DuplicateIndex.__eq__
                    continue

                if this.columns == that.columns:
                    if this.includes == that.includes:
                        #   EXACT duplicates means two indexes on the same table with the same columns in the same order
                        #   t1(c1, c2, c3) == t1(c1, c2, c3)
                        doubles[DuplicateIndex(table, this, that)] = Reason.EXACT
                        continue

                    elif this.includes.issuperset(that.includes) or this.includes.issubset(that.includes):
                        #   OVERLAPPING_INCLUDES
                        #   t1(c1, i2) vs t1(c1)
                        #   t1(c1, i2, i3) vs t1(c1, i3)

                        #   superset is the first table
                        if this.includes.issuperset(that.includes):
                            doubles[DuplicateIndex(table, this, that)] = Reason.OVERLAPPING_INCLUDES
                        else:
                            doubles[DuplicateIndex(table, that, this)] = Reason.OVERLAPPING_INCLUDES

                        continue

                    else:
                        #   DIFFERENT_INCLUDES means the indexes only differ in includes
                        #   t1(c1, i2) vs t1(c1, i3)
                        doubles[DuplicateIndex(table, this, that)] = Reason.DIFFERENT_INCLUDES
                        continue

                #   OVERLAP means one index has all columns in the same order as another one, plus one or more extra
                #   t1(c1, c2, c3, c4) overlaps t1(c1, c2) but not t1(c2, c3)
                elif this.columns[:len(that.columns)] == that.columns \
                        or that.columns[:len(this.columns)] == this.columns:
                    # index with most columns comes first
                    if len(this.columns) > len(that.columns):
                        doubles[DuplicateIndex(table, this, that)] = Reason.OVERLAP
                    else:
                        doubles[DuplicateIndex(table, that, this)] = Reason.OVERLAP
                    continue

    return doubles


def rows_to_dict(cur, sql):
    """ Convert a pyodbc.Row object to a list with dictionaries.
        Different versions of SQL Server return different results for Tables, Indexes etc.
        In order to be flexable we need to use **kwargs to create the instances instead of *args.
    """
    cursor = cur.execute(sql)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results


def main() -> int:
    if 'ODBC Driver 17 for SQL Server' in pyodbc.drivers():
        driver = 'ODBC Driver 17 for SQL Server'
    elif 'SQL Server Native Client 11.0' in pyodbc.drivers():
        driver = 'SQL Server Native Client 11.0'
    else:
        raise AssertionError("Can't find ODBC driver")

    server = os.environ['server']
    database = os.environ['database']
    app = "index-inspector"
    conn = pyodbc.connect(f"Driver={{{driver}}};Server={server};Database={database};Trusted_Connection=yes;APP={app}")
    cur = conn.cursor()

    sql = "select s.* from sys.schemas s join sys.tables t on s.schema_id = t.schema_id and t.is_ms_shipped = 0"
    schemas: dict[int, Schema] = \
        {row['schema_id']: Schema(**row)
         for row in rows_to_dict(cur, sql)}
    sql = "select * from sys.tables where is_ms_shipped = 0"
    tables: dict[int, Table] = \
        {row['object_id']: Table(**row)
         for row in rows_to_dict(cur, sql)}
    sql = "select c.* from sys.columns c join sys.tables t on c.object_id = t.object_id order by c.column_id"
    columns: dict[(int, int), Column] = \
        {(row['object_id'], row['column_id']): Column(**row)
         for row in rows_to_dict(cur, sql)}
    sql = "select i.* from sys.indexes i join sys.tables t on i.object_id = t.object_id"
    indexes: dict[(int, int), Index] = \
        {(row['object_id'], row['index_id']): Index(**row)
         for row in rows_to_dict(cur, sql)}
    sql = """
    select ic.*
    from sys.index_columns ic 
    join sys.columns c on ic.column_id = c.column_id and ic.object_id = c.object_id
    join sys.tables t on c.object_id = t.object_id
    order by object_id, index_id, index_column_id
    """
    index_columns: dict[(int, int, int), IndexColumn] = \
        {(row['object_id'], row['index_id'], row['index_column_id']): IndexColumn(**row)
         for row in rows_to_dict(cur, sql)}
    sql = "select * from sys.dm_db_index_usage_stats where database_id = DB_ID()"
    index_usage: dict[(int, int, int), IndexUsage] = \
        {(row['object_id'], row['index_id']): IndexUsage(**row)
         for row in rows_to_dict(cur, sql)}

    conn.close()

    schemas, tables, columns, indexes, index_columns, index_usage = connect_objects(schemas, tables, columns, indexes, index_columns, index_usage)
    doubles = inspect(tables)
    for duplicate, reason in doubles.items():
        print(duplicate, reason)

    pass
    return 0


if __name__ == "__main__":
    SystemExit(main())


# i = indexes[(864722133, 5)]
