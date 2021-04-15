#!/usr/bin/python3

# A Python program for gathering weather data from OpenWeatherMap

APPID = '0df1e954cdf7234460b02dcbd3f1b264'

import json, requests, sys

# Gets the location from command line arguments

if len(sys.argv) < 2:
	print("Error: need to enter city name and 2-letter country code")
	sys.exit()
print("Success")

print("Contents of sys.argv list ")
print(sys.argv[1:])
location = ''.join(sys.argv[1:])
print('Location: ' + location)

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APPID

response = requests.get(url)
response.raise_for_status()

WeatherData = json.loads(response.text)
print(WeatherData)
