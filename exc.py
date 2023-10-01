import requests

url = 'https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=City_Name'
def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 401:
        print('Ошибка: Неверный API ключ')
    elif response.status_code == 200:
        data = response.json()
        condition = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Конвертируем в градусы Цельсия

        print(f'Weather in {city}: {condition}')
        print(f'Температура: {temperature_celsius:.2f}°C')
    else:
        print('Ошибка: Не удалось получить данные о погоде')


# Ключ API и город для тестирования
api_key = '322ffa98323a03dda2c9ca1c37024395'
city = 'Киев'

get_weather(api_key, city)
