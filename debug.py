import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

print("Columns:")
df_info = pd.read_sql("PRAGMA table_info(orderDetails)", conn)
print(df_info[['name', 'type']].to_string(index=False))

print("\nFirst row:")
df_first = pd.read_sql("SELECT * FROM orderDetails LIMIT 1", conn)
print(df_first.to_dict('records'))

print("\nFirst 3 rows:")
print(pd.read_sql("SELECT * FROM orderDetails LIMIT 3", conn))

conn.close()
