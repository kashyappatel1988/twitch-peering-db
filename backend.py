#!/usr/bin/env python3 
import requests
import json
import urllib3
import pandas as pd
import sqlite3
from pprint import pprint

urllib3.disable_warnings()


### function to do an API call to the give url
def parser(url_name):
    req = requests.get(url_name, verify=False)
    op = json.loads(req.content)
    return op


def listtosqlite3(list, dbname, tablename,sortbycolumn=[],columnindex=[],columnstodrop=[]):
    conn = sqlite3.connect(dbname)
    df1 = pd.DataFrame(list)
    if columnstodrop: df1 = df1.drop(columns=columnstodrop)
    if columnindex:df1 = df1[columnindex]
    if sortbycolumn:df1.sort_values(by=sortbycolumn,inplace=True)
    if sortbycolumn:df1.reset_index(drop=True,inplace=True)
    # if columnindex: df1 = df1.columnsindex(columnindex,dtype='object')
    df1.index= df1.index+1
    df1.to_sql(tablename, conn,if_exists='replace')
    df1.to_csv(f'data/{tablename}.csv', index_label='index', encoding='utf-8')


# Backend DB tables
# main db = twitch-peering-backend-db
# 4 tables will be created for 4 tasks
# table1 = Orginfo
# table2 = private peering facilities
# table3 =  Public Peering exchange point
# table4 = Executive summary

# Initiate API calls to Peeringdb.com
if __name__ == "__main__":
    # API call for getting all  information
    baseurl = "https://peeringdb.com/api/net/1956"
    output = parser(baseurl)
    output_dict = (output['data'][0])  # <class 'dict'>
    public_peering_ex = output_dict['netixlan_set']  # <class 'list'>
    facilities = output_dict['netfac_set']  # <class 'list'>
    # API call for org specific information, could be done by running loops over exisiting output
    org_info_url = f'''https://peeringdb.com/api/org/{output_dict['org']['id']}'''
    output1 = parser(org_info_url)  # <class 'dict'>
    org_info = (output1['data'][0]['net_set'])  # <class 'list'>
    listtosqlite3(public_peering_ex,
                  'data/twitch-peering-db',
                  'public_peering',sortbycolumn=['name'],
                  columnstodrop=['ix_id', 'id', 'ixlan_id', 'is_rs_peer', 'notes', 'notes','operational'],
                  columnindex=['name','speed','ipaddr4','ipaddr6','asn','updated'])
    listtosqlite3(facilities,
                  'data/twitch-peering-db',
                  'facilities', columnstodrop=['id', 'fac_id','status'])
    listtosqlite3(org_info,
                  'data/twitch-peering-db',
                  'org_info', columnstodrop=['notes'])
