## Twitch Peering DB 

### Install Requirements
```pip3 install -r requirements.txt```

### Public URL 
http://www.twitchpeerdb.com/
### Start serverVia CLI 
```
make
```
http://127.0.0.1:5000/
### Example

```
make
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

### HTML CSS Bootstrap Templates source 
https://startbootstrap.com/themes/

### Backend Datasource 
https://www.peeringdb.com/

## Application Flow 
### Backend 
```
Backend file - Backend.py 
API calls 
1. API call to https://peeringdb.com/api/net/1956 
2. another API call for Org info  

Create two dict from the Output list
1. Private Peering Facilities  
2. Public Peering exchange points
3. Org info ( from 2nd API call) 

Create 3 tables of SQLITE3 
sqlite> .tables
facilities      org_info        public_peering
sqlite> 
```
### Frontend 
```
Frontend file - app.py 
Flask  @app.routes 
1. / - index.htmls 
2. /org - org-info.html
3. /private-facilities- private-facilites.html
4. /public-peering - public-peering.html
5. /summary - summary.html
```


