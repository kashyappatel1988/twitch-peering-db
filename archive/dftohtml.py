import sqlite3
import pandas as pd

DATABASE = '../data/twitch-peering-db'


def dict_factory(cursor, row):
    d = {}
    # print (cursor.description)
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def querydb_dict(databasename, cmd):
    conn = sqlite3.connect(databasename)
    # print (conn.row_factory)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(cmd)
    output = cur.fetchall()
    return output
def querydb(databasename,cmd):
    conn = sqlite3.connect(databasename)
    cur = conn.cursor()
    cur.execute(cmd)
    output = cur.fetchall()
    return output

# cmd = "select * from public_peering"
cmd = "select sum(speed) from public_peering"
# cmd = "select sum(speed) from public_peering"

def summary():
    output = []
    cmd1 = 'SELECT sum(speed) from public_peering'
    cmd2 = 'SELECT distinct name from public_peering'
    cmd3 = 'SELECT distinct name  from facilities'
    total_speed = querydb_dict(DATABASE,cmd1)
    unique_public_peerings=querydb(DATABASE,cmd2)
    unique_private_peerings=querydb(DATABASE,cmd3)
    unique_public_peerings= (len(unique_public_peerings))
    unique_private_peerings= (len(unique_private_peerings))
    output = [{'1':total_speed},{"2":unique_public_peerings},
              {'3':unique_private_peerings}]
    return output


    # output.extend(unique_peetings)
    # facilities_length= (len(facilities))
    # output.append(facilities_length)
    # output.extend(total_speed)
    # return output

output= (summary())
print (output)
# print (output[0]['total_speed'][0]['sum(speed)'])
# print (len(output[1]['unique_public_peerings']))
# print (len(output[2]['unique_private_peerings']))

# for member in (l[1]['unique_public_peerings']):
#     print (str(member[0]))
# print (l[1]['unique_public_peerings'])
# m= (l[0]['total_speed'][0])
# print (type(m))
# # l1 = querydb(DATABASE, cmd)
# print(str(l1[0]))
# print (type(l1))

#
# df= pd.DataFrame(l1)
# df.to_html('test.html')
#
# op = summary()
# key = str(op[-1].keys())
# print (key)
#
# print (op[-1]['sum(speed)'])