import requests
from flask import Flask

app = Flask(__name__)

url = 'http://api.openweathermap.org/data/2.5/weather?appid=932101dce842f87527bad4bc2fe1b2b6&units=metric&q='

@app.route('/')
def index():
    return "Put a city in the url, like so: <a href="ignat.pythonanywhere.com/london">ignat.pythonanywhere.com/london</a>"

@app.route('/<cityname>')
def city(cityname):

    try:
        apiCall = url + cityname
        data = requests.get(apiCall).json()
        returnedCity = data['name']
        returnedCountry = data['sys']['country']
        temp = data['main']['temp']

        if cityname.lower() == returnedCity.lower():
            return 'It is {}°C in {}, {}'.format(temp, returnedCity.capitalize(), returnedCountry)
        else:
            return 'Not sure what you mean by "{}", but here is the temperature in {}, {}: {}°C'.format(cityname, returnedCity, returnedCountry, temp)

    except KeyError:
        return 'Try some other city'

