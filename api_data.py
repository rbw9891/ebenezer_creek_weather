# dependencies
import requests
import json
from api_key import accu_api
import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database
db = client.ebenezer_db

# Drops collection if available to remove duplicates
db.weather.drop()

# Connect to collection
weather = db.weather

def api_get():
    
    # create url and requests variables
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/2153253?apikey={accu_api}"
    r = requests.get(url)
    r_json = r.json()

    # empty dict for daily weather
    daily_weather = {}

    

