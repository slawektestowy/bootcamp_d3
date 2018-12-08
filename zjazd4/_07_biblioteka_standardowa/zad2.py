# Napisz program wyswietlajacy pogode dla wskazanej przez
# uzytkownika lokalizacji.
# Skorzystaj z modułu urllib.request, json oraz API
# MetaWeather.
# https://www.metaweather.com/api/location/search/?query=(query)
# https://www.metaweather.com/api/location/(woeid)/
import urllib.request
import json

URL_LOCATION = 'https://www.metaweather.com/api/location/search/?query='
URL_WEATHER = 'https://www.metaweather.com/api/location/'

url = URL_LOCATION + input('podaj lokalizację: ')
with urllib.request.urlopen(url) as source:
    # loads dostaje na pierwszym parametrze string
    # dane = json.loads(source.read(),encoding='utf-8')
    # dane = json.loads(source.read().decode('utf-8'))

    # load dostaje na pierwszym parametrze źródło danych
    dane = json.load(source)
# print(dane)
woeid = dane[0]['woeid']

url = URL_WEATHER + str(woeid)
with urllib.request.urlopen(url) as source:
    dane = json.load(source)
# print(dane)

pogoda = dane['consolidated_weather'][0]
print('ogolnie:', pogoda['weather_state_name'])
print('wiatr:', pogoda['wind_direction_compass'])
print('temp:', pogoda['the_temp'])
print('wilgotność:', pogoda['humidity'])
