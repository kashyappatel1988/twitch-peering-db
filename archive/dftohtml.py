import sqlite3
import pandas as pd

DATABASE = 'data/twitch-peering-db'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def dbconnect(databasename, cmd):
    conn = sqlite3.connect(databasename)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(cmd)
    output = cur.fetchall()
    return output


cmd = "SELECT * from public_peering"

l1 = dbconnect(DATABASE, cmd)
df= pd.DataFrame(l1)
df.to_html('test.html')