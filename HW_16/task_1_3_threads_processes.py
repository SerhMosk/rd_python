# Task 1. Use https://open-meteo.com/ to get the weather forecast for
# 5 of your favorite cities on the planet. Implement using the requests
# module using multithreading and multiprocessing.
#
# Task 2. Find the average temperature according to the forecast for each
# city and display which city is currently the hottest.
#
# Task 3. Derive the difference in program execution time using streams and processes.

import datetime as dt
import time
import requests
import threading
import multiprocessing as mp

sep_num = 30
api_url = "https://api.open-meteo.com/v1/forecast"
favorite_cities = [
    {"id": 1, "name": "Kryvyi Rih", "latitude": 47.91, "longitude": 33.39, "temperature_list": [], "average": 0},
    {"id": 2, "name": "Kyiv", "latitude": 50.45, "longitude": 30.52, "temperature_list": [], "average": 0},
    {"id": 3, "name": "New York", "latitude": 40.71, "longitude": -74.01, "temperature_list": [], "average": 0},
    {"id": 4, "name": "London", "latitude": 51.51, "longitude": -0.13, "temperature_list": [], "average": 0},
    {"id": 5, "name": "Tokyo", "latitude": 35.69, "longitude": 139.69, "temperature_list": [], "average": 0},
]


def print_sep(symbol, brl="\n"):
    print(brl + (symbol * sep_num))


def request(city):
    print(f"Request Start of {city.get('id')}")

    resp = requests.get(
        url=api_url,
        params={
            "latitude": city.get('latitude'),
            "longitude": city.get('longitude'),
            "hourly": "temperature_2m",
        }
    )

    # temperatures can be analyzed and used
    temperature_list = resp.json()["hourly"]["temperature_2m"]
    city['temperature_list'] = temperature_list
    city['average'] = sum(temperature_list) / len(temperature_list)

    print(f"Request End of {city.get('id')}")
    return city


def analyze_data(results):
    if len(results) > 0:
        hot_city = results[0]

        for result in results:
            print(f"City: {result.get('name')}. Average temperature: {result.get('average')}°С")
            if result.get('average') > hot_city.get('average'):
                hot_city = result

        print_sep("-", "")

        print(f'Now: {dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}')
        print(f"The hottest city now is {hot_city.get('name')}.\nAverage temperature is {hot_city.get('average')}°С")
        # ------------------------------
        # Now: 29.04.2023 14:21:00
        # The hottest city now is Tokyo.
        # Average temperature is 18.04404761904762°С


def multi_thread():
    start = time.time()
    threads = []
    results = []

    def thread_request(city):
        results.append(request(city))

    print("MULTITHREADING")
    print_sep("-", "")

    for item in favorite_cities:
        threads.append(threading.Thread(target=thread_request, args=(item, )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    analyze_data(results)

    end = time.time()
    print(f"Multithreading time is {end - start}")
    return end - start


def process_request(city, queue):
    res = request(city)
    queue.put(res)


def multi_process():
    start = time.time()
    processes = []
    results = []
    q = mp.Queue()

    print("MULTIPROCESSING QUEUE")
    print_sep("-", "")

    for item in favorite_cities:
        p = mp.Process(target=process_request, args=(item, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for _ in favorite_cities:
        results.append(q.get())

    analyze_data(results)

    end = time.time()
    print(f"Multiprocessing time is {end - start}")
    return end - start


def multi_process_pool():
    start = time.time()

    print("MULTIPROCESSING POOL")
    print_sep("-", "")

    with mp.Pool(processes=5) as pool:
        results = pool.map(request, favorite_cities)

    analyze_data(results)

    end = time.time()
    print(f"Multiprocessing time is {end - start}")
    return end - start


def compare_speed(results):
    fast_method = results[0]
    for item in results:
        print(f"{item.get('type')} time: {item.get('time')} second")
        if fast_method.get('time') > item.get('time'):
            fast_method = item

    print_sep("-", "")
    print(f"FASTEST METHOD: {fast_method.get('type')}\nTIME: {fast_method.get('time')} second")


if __name__ == "__main__":
    mt_time = multi_thread()
    print_sep("=")

    mpq_time = multi_process()
    print_sep("=")

    mpp_time = multi_process_pool()
    print_sep("=")

    all_results = [
        {"type": "Multithreading", "time": mt_time},
        {"type": "Multiprocessing Queue", "time": mpq_time},
        {"type": "Multiprocessing Pool", "time": mpp_time},
    ]
    compare_speed(all_results)

# ==============================
# Multithreading time: 0.19386816024780273 second
# Multiprocessing Queue time: 0.30534887313842773 second
# Multiprocessing Pool time: 0.2744789123535156 second
# ------------------------------
# FASTEST METHOD: Multithreading
# TIME: 0.19386816024780273 second
