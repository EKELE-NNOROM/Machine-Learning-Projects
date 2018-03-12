import sqlite3
from pprint import pprint

cur = sqlite3.connect('factbook.db').cursor()
cur.execute("select * from facts order by population asc limit 10;")
data = cur.fetchall()
cur.close()
pprint(data)

con = sqlite3.connect('factbook.db')
facts = pd.read_sql_query("select * from facts;", con)
con.close()
