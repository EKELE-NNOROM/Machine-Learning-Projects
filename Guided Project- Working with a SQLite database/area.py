import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')
area = pd.read_sql_query("select sum(area_land)/sum(area_water) from facts;", conn)
print(area)
conn.close()