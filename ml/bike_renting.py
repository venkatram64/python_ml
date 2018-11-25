import calendar
import numpy as np
import pandas as pd
import missingno as msno
from datetime import datetime

data = pd.read_csv('hour.csv', sep=',')

#print(data)

# Separate the date
seasonMap = {1: "Spring", 2 : "Summer", 3 : "Fall", 4 :"Winter" }
weatherMap = {1: " Clear + Few clouds + Partly cloudy + Partly cloudy",\
              2 : " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ", \
              3 : " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", \
              4 :" Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog " }

data["date"] = data.dteday.apply(lambda x : x.split()[0])
data["weekday"] = data.date.apply(lambda dateString : calendar.day_name[datetime.strptime(dateString,"%Y-%m-%d").weekday()])
data["season"] = data.season.map(seasonMap)
data["weather"] = data.weathersit.map(weatherMap)

categoryVariableList = ["hr", "weekday", "mnth", "season", "weather", "holiday", "workingday"]
for var in categoryVariableList:
    data[var] = data[var].astype("category")

data = data.drop(["dteday"], axis=1)

# Missing data detection
msno.matrix(data, figsize=(10, 3))

print(data)