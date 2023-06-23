# Task 2. Using the weather API https://open-meteo.com/en/docs, write a program
# that will accept the name of the city from the user and output the current
# weather data to the console.
# To determine the coordinates of the city, you can use
# https://open-meteo.com/en/docs/geocoding-api
# Or you can use any other API for your ideas.

import requests
from datetime import datetime as dt

GEOCODING_API = 'https://geocoding-api.open-meteo.com/v1/search'
WEATHER_API = 'https://api.open-meteo.com/v1/forecast'


def get_coords(city):
    res = requests.get(url=GEOCODING_API, params={"name": city})

    results = res.json().get('results')

    if isinstance(results, list):
        return results[0]

    return None


def get_weather(coords):
    params = {
        "latitude": coords.get('latitude'),
        "longitude": coords.get('longitude'),
        "current_weather": True,
    }
    res = requests.get(url=WEATHER_API, params=params)

    return res.json().get('current_weather')


def init_app():
    print('--- GET WEATHER IN THE CITY ---')
    print('Enter "exit" to stop program')

    while True:
        command = input('ENTER CITY NAME: ')

        if command == '':
            continue

        elif command == 'exit':
            break

        print(f"Request Coords Start")
        print('=' * 30)
        coords = get_coords(command)
        # print(coords)
        if coords:
            print(f'Coords: longitude = {coords["longitude"]}, latitude = {coords["latitude"]}')
            print('-' * 30)

            print(f"Request Weather Start")
            print('=' * 30)
            if weather := get_weather(coords):
                print(f'Weather in {command}')
                for key in weather.keys():
                    print(f'- {key}: {dt.strptime(weather[key], "%Y-%m-%dT%H:%M").strftime("%d.%m.%Y %H:%M") if key == "time" else weather[key]}')
            else:
                print('Weather not found. Try again.')
            print('-' * 30)

        else:
            print('City not found. Try again.')
            print('-' * 30)


# Run program
init_app()

