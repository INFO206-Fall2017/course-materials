# daily.py
# 
# Provides the weather for Berkeley, CA for today

from urllib.request import urlopen
import json

def forecast():
    """
    Returns the daily weather for Berkeley, CA
    """
    response = urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?q=Berkeley&mode=json&units=Imperial&cnt=1&appid=7dc34849d7e8b6fbdcb3f12454c92e88')
    rawWeatherData = response.read().decode("utf-8")
    weatherData = json.loads(rawWeatherData)

    forecastStr = "Forecast for Berkeley, CA: " + weatherData["list"][0]["weather"][0]["main"] + "\n" \
        "Current Temp: " + str(weatherData["list"][0]["temp"]["day"]) + " degrees \n"  \
        "High Temp: " + str(weatherData["list"][0]["temp"]["max"]) + " degrees \n" \
        "Low Temp: " + str(weatherData["list"][0]["temp"]["min"]) + " degrees"

    return forecastStr