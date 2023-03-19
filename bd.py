import sqlite3
import requests
import ast
from bs4 import BeautifulSoup as bs


db = sqlite3.connect('predprof.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS polet (
  id INTEGER PRIMARY KEY,
  SH INTEGER,
  distance INTEGER
);""")
db.commit()

r = requests.get('https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token': 'xzu72dde'})
put = bs(r.text, 'html.parser').text
put = put.replace("\n", "")
put = put.replace(' ', '')
put = ast.literal_eval(put)
polet = []
for i, j in put.items():
  for k in j:
    for ii, jj in k.items():
      for kk in jj:
        polet.append(kk)

add_to_db = """INSERT INTO polet (SH, distance) VALUES (?, ?)"""
for i in polet:
  cursor.execute(add_to_db, (i['SH'], i['distance']))
  db.commit()

rows = cursor.execute('''SELECT * FROM polet''').fetchall()
rows_idnew = []
for i in rows:
    rows_idnew.append(i)

print(polet)
print(rows_idnew)
