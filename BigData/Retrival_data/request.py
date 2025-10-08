import requests

# city_name = "Bologna"
lat = 44.4667
lon = 11.4333
api_key = "c9f9c0dcba2d40f19ca2af247c5d4045"
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
# URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
data = requests.get(URL)
# print(data.status_code) # value of status 200 - 400 - 500
print(data.json())
# print(data.url)