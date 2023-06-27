# Flask
# 1. Create a Flask application in the repository with homework in a separate flask-homework directory.
# - All further Flask homework should be done in this directory by making the necessary changes.
# - As part of the Flask theme, you don't need to create new directories every time for a new homework.
# 2. Install Flask and create a flask application with a hello (GET) endpoint. The endpoint should return
# the text "Hello, world!". (http://localhost:5000/hello)
# 3. Add two more endpoints: one to return html, the other - json
# 4. Configure logging in any format. Add INFO logs to all three functions.

from flask import Flask
from logging.config import dictConfig
import requests

GEOCODING_API = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_API = 'https://api.open-meteo.com/v1/forecast'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)


def get_coords(city):
    res = requests.get(url=GEOCODING_API, params={"name": city})

    results = res.json().get('results')

    if isinstance(results, list):
        return results[0]

    return {}


def get_weather(coords):
    params = {
        "latitude": coords.get('latitude'),
        "longitude": coords.get('longitude'),
        "current_weather": True,
    }
    res = requests.get(url=WEATHER_API, params=params)

    return res.json().get('current_weather')


@app.route('/')
def home_page():
    app.logger.info('GET Home page')

    return (
        '<h1>Home Page</h1>'
        '<p>The endpoint should return the text "Hello, world!": <a href="/hello">Hello Page</a></p>'
        '<p>The endpoint should return the HTML: <a href="/html">HTML Page</a></p>'
        '<p>The endpoint should return the JSON: <a href="/weather">Get Weather in city</a></p>'
    )


@app.route('/hello')
def hello_page():
    hello = 'Hello, world!'
    app.logger.info(f'GET Text "{hello}"')

    return (
        hello
    )


@app.route('/html')
def html_page():
    app.logger.info('GET HTML page')

    return (
        '<h1>HTML Page</h1>'
        '<a href="/">Home Page</a>'
    )


@app.route('/weather')
def weather_json():
    app.logger.info('GET Weather json')

    city = 'Kryvyi Rih'
    coords = get_coords(city)

    if coords:
        return get_weather(coords)
    return {}


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
