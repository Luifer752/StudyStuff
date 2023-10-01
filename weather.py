import requests

API_KEY = '322ffa98323a03dda2c9ca1c37024395'


def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # condition = data['weather'][0]['description']
        temp_c = data['main']['temp'] - 273.15

        print(f"The weather in {city} is {int(temp_c)}°C")

    elif response.status_code == 401:
        print("Wrong API key")

    else:
        print("Unknown Error")


city = input("Please enter the city:")

get_weather(API_KEY, city)
