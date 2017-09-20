# weekly.py
# 
# Provides the weather for Berkeley, CA for the week

from urllib.request import urlopen
import json
import datetime

def forecast():
    """
    Returns the daily weather for Berkeley, CA
    """
    response = urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?q=Berkeley&mode=json&units=Imperial&cnt=7&appid=7dc34849d7e8b6fbdcb3f12454c92e88')
    rawWeatherDataList = response.read().decode("utf-8")
    weatherDataList = json.loads(rawWeatherDataList)

    forecastStr = ""
    for i in range(7):
        forecastStr += _daily_forecast(weatherDataList["list"][i]) + "\n\n"

    forecastStr = forecastStr[:-2] # Remove the two newlines at the end 
    return forecastStr


def _daily_forecast(weatherData):
    """
    Helper function that prints a single day's forecast
    """

    # Using python datetime support to convert a timestamp into a full date
    
    # First need to define the UTC offset for Berkeley, CA (UTC - 8:00) (not daylight savings time)
    current_utc_offset = -datetime.timedelta(hours=8)

    # Next we create a timezone based on the utc offset for Pacific Standard Time
    current_timezone = datetime.timezone(current_utc_offset)

    # Last we create a datetime object based on the timestamp provided by the response, and
    # we localize the timezone to represent Pacific Standard Time 
    current_datetime = datetime.datetime.fromtimestamp(weatherData["dt"], current_timezone)

    # Printing of the forecast
    
    # Note we use strftime to format how we would like to print out the datetime
    forecastStr = "Forecast for Berkeley, CA on " + current_datetime.strftime("%A, %B %d, %Y %H:%M %p") + " local time\n" \
    "Weather: "  + weatherData["weather"][0]["main"] + "\n" \
    "Current Temp: " + str(weatherData["temp"]["day"]) + " degrees \n"  \
    "High Temp: " + str(weatherData["temp"]["max"]) + " degrees \n" \
    "Low Temp: " + str(weatherData["temp"]["min"]) + " degrees"

    return forecastStr
