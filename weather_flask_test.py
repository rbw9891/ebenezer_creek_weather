from flask import Flask
import requests
import json
import pandas as pd
from api_key import accu_api
from PIL import Image

url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/2153253?apikey={accu_api}"

r = requests.get(url)
r_json = r.json()

max_temp = r_json["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
daily_precip = r_json["DailyForecasts"][0]["Day"]["HasPrecipitation"]
date = r_json["DailyForecasts"][0]["Date"]

# create a list of the index for all 5 days within dictionary
day_index = [0,1,2,3,4]
# create empty lists for use in df
temp = []
precip = []
day_date = []

# loop through response dictionary and append values to empty lists 
for days in day_index:
    temp.append(r_json["DailyForecasts"][days]["Temperature"]["Maximum"]["Value"])
    precip.append(r_json["DailyForecasts"][days]["Day"]["HasPrecipitation"])
    day_date.append(r_json["DailyForecasts"][days]["Date"])

# create df with newly appened lists
five_day_df = pd.DataFrame({"Date":day_date,
                           "Temperature":temp,
                           "Precipitation":precip})

# create variables for day temps using iloc
today_temp = five_day_df.iloc[0,1]
tomorrow_temp = five_day_df.iloc[1,1]
next_day_temp = five_day_df.iloc[2,1]

# create variables for precip using iloc
today_precip = five_day_df.iloc[0,2]
tomorrow_precip = five_day_df.iloc[1,2]
next_day_precip = five_day_df.iloc[2,2]

# think i need to define functions of conditionals to output proper clothing
# def clothing():
# image.open() for Bren's illustrations

img_shorts = Image.open('boardshorts.jpg')


def clothing_1(temp_1,precip_1):
    if temp_1 > 72.5 and precip_1 == False:
        print("Board shorts and t-shirt")
        img_shorts.show()
    else:
        print("Stay Home")

clothing_1(today_temp,today_precip)

# not working. look into flask more and how to import all of the original script into flask
# app = Flask(__name__)

# @app.route("/")
# def home():
    # print("i think it works")
    # return clothing_1(today_temp,today_precip)
        
# if __name__ == "__main__":
    # app.run(debug=True)