from flask import Flask, render_template, g
import sqlite3
import pandas as pd

app = Flask(__name__, static_folder="static")

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


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/org", methods=["GET"])
def org():
    cmd = '''SELECT * from org_info '''
    cur = dbconnect(DATABASE, cmd)
    return render_template("org-info.html", output=cur)


@app.route("/private-facilities", methods=["GET"])
def private_facilities():
    cmd = 'SELECT * from facilities'
    cur = dbconnect(DATABASE, cmd)
    return render_template("private-facilities.html", output=cur)


@app.route("/public-peering", methods=["GET"])
def public_peering():
    cmd = 'SELECT * from public_peering'
    cur = dbconnect(DATABASE, cmd)
    return render_template("public-peering.html", output=cur)


if __name__ == "__main__":
    app.run(debug=True)

# cmd = 'SELECT id,name,aka,website from org_info'
# print(dbconnect(DATABASE,cmd))
