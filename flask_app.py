import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

import requests


app = Flask(__name__)

# response_location = requests.get("http://soil-monitoring-system.herokuapp.com/location")
# dict_location = response_location.json()
# print(dict_location)

# response_weather = requests.get("http://soil-monitoring-system.herokuapp.com/weather")
# dict_weather = response_weather.json()
# print(dict_weather)

# response_sensors = requests.get("http://soil-monitoring-system.herokuapp.com/sensors")
# dict_sensors = response_sensors.json()
# print(dict_sensors)

response_predictions = requests.get("http://soil-monitoring-system.herokuapp.com/predictions")
dict_predictions = response_predictions.json()
# print(dict_predictions)

# def get_city():
#     response_location = requests.get("http://soil-monitoring-system.herokuapp.com/location")
#     dict_loc = response_location.json()
#     return(dict_loc['location_data']['name'])


@app.route('/', methods=['GET', 'POST'])
def home():

    # dict_weather = {"weather_data": {"observation_time": "08:41 AM", "temperature": 18, "weather_code": 143, "weather_icons": ["https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0006_mist.png"], "weather_descriptions": ["Haze"], "wind_speed": 6, "wind_degree": 100, "wind_dir": "E", "pressure": 1019, "precip": 0.1, "humidity": 73, "cloudcover": 50, "feelslike": 18, "uv_index": 4, "visibility": 4, "is_day": "yes"}, "Alerts": {"safety_measures": "All good right now."}}

    # dict_location = {"location_data": {"name": "Bhopal", "country": "India", "region": "Madhya Pradesh", "lat": "23.267", "lon": "77.400", "timezone_id": "Asia/Kolkata", "localtime": "2019-12-16 14:11", "localtime_epoch": 1576505460, "utc_offset": "5.50"}, "Recommended_crops": {"crops_suitable": ["Wheat", "Gram", "Mustard", "Sugarcane", "Sun Flower", "Pea", "Linseed", "Banana"]}}

    # dict_sensors = {"sensor_data": {"Temperature": "23.00", "Humidity": "63.00", "Carbon_Monoxide": "0.04", "Nitrates": "1.88", "Soil_Moisture": "454.00", "Smoke": "null", "Color_Indicator": "null"}, "Soil_Moisture": {"condition": "In suitable range", "soil_respiration": "Optimal", "counter_measures": "Not Required right now!"}, "Fire_&_CO": {"condition": "CO levels in safe range."}, "Denitrification": {"condition": "Nitrate levels in safe range."}}


    response_location = requests.get("http://soil-monitoring-system.herokuapp.com/location")
    dict_loc = response_location.json()
    print(dict_loc)

    response_weather = requests.get("http://soil-monitoring-system.herokuapp.com/weather")
    dict_weather = response_weather.json()
    print(dict_weather)

    response_sensors = requests.get("http://soil-monitoring-system.herokuapp.com/sensors")
    dict_sensors = response_sensors.json()
    print(dict_sensors)

    city = dict_loc['location_data']['name']
    temp = dict_weather['weather_data']['temperature']
    humidity = dict_sensors['sensor_data']['Humidity']
    wind_speed = dict_weather['weather_data']['wind_speed']
    soil_moisture = dict_sensors['sensor_data']['Soil_Moisture']
    soil_moisture = (1-float(soil_moisture)/1024)*100
    recommended_crops = str(",".join(dict_predictions['crops_suitable']))
    #print(recommended_crops)
    denitrification = str(dict_sensors['Denitrification']['condition'])
    print(denitrification)
    fire = (dict_sensors['Fire_&_CO']['condition'])
    print(fire)
    weather = dict_weather['weather_data']['weather_descriptions'][0]
    pressure = dict_weather['weather_data']['pressure']
    precipitation = dict_weather['weather_data']['precip']
    uv = dict_weather['weather_data']['uv_index']
    soil_moisture = dict_sensors['Soil_Moisture']['condition']


    return render_template('index5.html', uv = uv, city = city, temp = temp,recommended_crops = recommended_crops, humidity = humidity, wind_speed = wind_speed, soil_moisture = soil_moisture, fire = fire, denitrification = denitrification, pressure = pressure, precipitation = precipitation, weather = weather)

# # lat, lon = get_lat_and_lon()
# # print(lat, lon)







if __name__ == "__main__":
    app.run(debug=True)