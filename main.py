import os
from collections import defaultdict
from enum import Enum
from objects import Schema, Table, Column, Index, IndexColumn

import pyodbc


class Reason(Enum):
    EXACT = 1
    OVERLAP = 2
    ALMOST = 3
    INCLUDE = 4


def connect_objects(schemas, tables, columns, indexes, index_columns):
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
            tables[index.object_id].indexes.add(index)

    for index_column in index_columns.values():
        index_column.name = columns[(index_column.object_id, index_column.column_id)].name
        if (index_column.object_id, index_column.index_id) in indexes:
            if index_column.is_included_column:
                indexes[(index_column.object_id, index_column.index_id)].includes.add(index_column)
            else:
                indexes[(index_column.object_id, index_column.index_id)].columns.append(index_column)


class Inspect():

    def __init__(self):
        pass

    def __init__(self, reason: Reason, object_id_1: int, index_id_1: int, object_id_2: int, index_id_2: int):
        self.reason = reason
        self.object_id_1 = object_id_1
        self.index_id_1 = index_id_1
        self.object_id_2 = object_id_2
        self.index_id_2 = index_id_2

    @classmethod
    def from_dicts(cls, reason: Reason, this_index, other_index):
        pass


def duplicate_columns(indexes):
    duplicates = []
    exact_duplicates = []
    overlap_duplicates = []
    almost_duplicates = []
    last_column_included = []

    seen = set()
    for this_key, this_value in indexes.items():
        this_object_id, this_index_id = this_key
        for other_key, other_value in indexes.items():
            if this_key == other_key:  # don't compare to self
                continue
            other_object_id, other_index_id = other_key
            if this_object_id != other_object_id:  # only compare to same table
                continue

            key = (this_object_id, min(this_index_id, other_index_id), max(this_index_id, other_index_id))
            if key in seen:  # we have already compared these two
                continue

            seen.add(key)

            if this_value['columns'] == other_value['columns']:
                duplicates.append(Inspect.from_dict(Reason.EXACT, this_value, other_value))
                print(
                    f"{this_value['table_name']} has duplicate columns for {this_value['index_name']} and {other_value['index_name']}")
                exact_duplicates.append((this_key, other_key))
                continue
            elif this_value['columns'][:len(other_value['columns'])] == other_value['columns'] \
                    or other_value['columns'][:len(this_value['columns'])] == this_value['columns']:
                # overlapping means index on [col1, col2, col3, col4] overlaps index on [col1, col2]
                # but not index on [col2, col3]
                print(
                    f"{this_value['table_name']} has overlapping duplicate columns for {this_value['index_name']} and {other_value['index_name']}")
                overlap_duplicates.append((this_key, other_key))
                continue

            # last_column_included finds these kind of indexes:
            #     idx1: [col1, col2, col3] include []
            #     idx2: [col1, col2] include [col3]
            # idx2 is not needed here
            elif (this_value['columns'][:len(other_value['columns']) - 1] == other_value['columns']
                  and other_value['columns'][-1] in other_value['includes']) or \
                    (other_value['columns'][:len(this_value['columns']) - 1] == this_value['columns']
                     and this_value['columns'][-1] in this_value['includes']):
                print(f"found last_column_included error")

    return exact_duplicates


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


def main():
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

    schemas: dict[int, Schema] = \
        {row['schema_id']: Schema(**row)
         for row in rows_to_dict(cur, "select * from sys.schemas")}
    tables: dict[int, Table] = \
        {row['object_id']: Table(**row)
         for row in rows_to_dict(cur, "select * from sys.tables")}
    columns: dict[(int, int), Column] = \
        {(row['object_id'], row['column_id']): Column(**row)
         for row in rows_to_dict(cur, "select * from sys.columns")}
    indexes: dict[(int, int), Index] = \
        {(row['object_id'], row['index_id']): Index(**row)
         for row in rows_to_dict(cur, "select * from sys.indexes")}
    index_columns: dict[(int, int, int), IndexColumn] = \
        {(row['object_id'], row['index_id'], row['index_column_id']): IndexColumn(**row)
         for row in rows_to_dict(cur, "select * from sys.index_columns")}

    conn.close()

    connect_objects(schemas, tables, columns, indexes, index_columns)
    pass


if __name__ == "__main__":
    SystemExit(main())
