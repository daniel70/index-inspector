import os
import pathlib

import pyodbc




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

schemas: dict[int, Schema] = {row.schema_id: Schema(*row) for row in cur.execute("select * from sys.schemas").fetchall()}
conn.close()