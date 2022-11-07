import os
from collections import defaultdict

import pyodbc
import pathlib


def duplicate_columns(indexes):
    exact_duplicates = []
    almost_duplicates = []

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
                print(f"{this_value['table_name']} has duplicate columns for {this_value['index_name']} and {other_value['index_name']}")
                exact_duplicates.append((this_key, other_key))

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
