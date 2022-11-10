import os
from collections import defaultdict
from enum import Enum
from dataclasses import dataclass

import pyodbc
import pathlib


class Reason(Enum):
    EXACT = 1
    OVERLAP = 2
    ALMOST = 3
    INCLUDE = 4


@dataclass()
class Index:
    table_name: str
    index_name: str
    type: int
    type_desc: str
    is_unique: bool
    ignore_dup_key: bool
    is_primary_key: bool
    is_unique_constraint: bool
    is_hypothetical: bool
    has_filter: bool
    columns: list[Column] | None = None
    includes: set[Column] | None = None


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
    def from_dicts(cls, reason:Reason, this_index, other_index):
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


def transform_indexes(rows):
    indexes = defaultdict(dict)
    for row in rows:
        key = (row.object_id, row.index_id)
        if key not in indexes:
            indexes[key] = {
                'table_name': row.table_name,
                'index_name': row.index_name,
                'type': row.type,
                'type_desc': row.type_desc,
                'is_unique': row.is_unique,
                'ignore_dup_key': row.ignore_dup_key,
                'is_primary_key': row.is_primary_key,
                'is_unique_constraint': row.is_unique_constraint,
                'is_hypothetical': row.is_hypothetical,
                'has_filter': row.has_filter,
                'columns': list(),
                'includes': set(),
            }
        if row.is_included_column == 0:
            indexes[key]['columns'].append(row.column_id)
        else:
            indexes[key]['includes'].add(row.column_id)
    return indexes


def main():
    if 'ODBC Driver 17 for SQL Server' in pyodbc.drivers():
        driver = 'ODBC Driver 17 for SQL Server'
    elif 'SQL Server Native Client 11.0' in pyodbc.drivers():
        driver = 'SQL Server Native Client 11.0'
    else:
        raise AssertionError("Can't find ODBC driver")

    server = os.environ['server']
    database = os.environ['database']
    sql_dir = pathlib.Path(__file__).parent / "sql"
    sql_indices = open(sql_dir / "indices.sql").read()

    conn = pyodbc.connect(f"Driver={{{driver}}};Server={server};Database={database};Trusted_Connection=yes")
    cur = conn.cursor()
    rows = cur.execute(sql_indices).fetchall()
    indexes = transform_indexes(rows=rows)
    duplicates = duplicate_columns(indexes=indexes)
    conn.close()


if __name__ == "__main__":
    SystemExit(main())
