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

def querydb(databasename,cmd):
    conn = sqlite3.connect(databasename)
    cur = conn.cursor()
    cur.execute(cmd)
    output = cur.fetchall()
    return output

def querydb_dict(databasename,cmd):
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
    cur = querydb_dict(DATABASE, cmd)
    return render_template("org-info.html", output=cur)


@app.route("/private-facilities", methods=["GET"])
def private_facilities():
    cmd = 'SELECT * from facilities'
    cur = querydb_dict(DATABASE, cmd)
    return render_template("private-facilities.html", output=cur)


@app.route("/public-peering", methods=["GET"])
def public_peering():
    cmd = 'SELECT * from public_peering'
    cur = querydb_dict(DATABASE, cmd)
    return render_template("public-peering.html", output=cur)

@app.route("/summary",methods=["GET"])
def summary():
    output = []
    cmd1 = 'SELECT sum(speed) from public_peering'
    cmd2 = 'SELECT distinct name from public_peering'
    cmd3 = 'SELECT distinct name  from facilities'
    total_speed = querydb_dict(DATABASE,cmd1)
    unique_public_peerings=querydb(DATABASE,cmd2)
    unique_private_peerings=querydb(DATABASE,cmd3)
    unique_public_peerings = (len(unique_public_peerings))
    unique_private_peerings=(len(unique_private_peerings))
    output = [{'0':total_speed},{"1":unique_public_peerings},
              {'2':unique_private_peerings}]
    return render_template("summary.html",output=output)



if __name__ == "__main__":
    app.run(debug=True)

# cmd = 'SELECT id,name,aka,website from org_info'
# print(dbconnect(DATABASE,cmd))
