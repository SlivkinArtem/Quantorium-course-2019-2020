from pprint import pprint
#data[0] descr
import requests

city_id = '485239'
appid = '8be2336bf0e5e7ed40d23b4bd3ef565a'

request = requests.get('http://api.openweathermap.org/data/2.5/weather',
                       params = {'id' : city_id, 'APPID' : appid, 'units': 'metric', 'lang' : 'ru'})
data = request.json()
# pprint(data)
print(f"Погода : {data['weather'][0]['description']}")
print(f"Город : {data['name']}")
print(f"Температура : {data['main']['temp']}")
print(f"По ощущениям : {data['main']['feels_like']}")
print(f"Влажность : {data['main']['humidity']}")
print(f"Давление : {data ['main']['pressure']}")



