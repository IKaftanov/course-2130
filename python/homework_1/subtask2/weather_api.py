import requests
from tokens import YANDEX_WEATHER_API_KEY

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key, api_url):
        self.api_key = YANDEX_WEATHER_API_KEY
        self.api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def get_current_weather(self, lat, lon):
        api_url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        response = requests.get(self.api_url, headers={'X-Yandex-API-Key': self.api_key})
        print(response.json())
        """
            TODO: return a weather for current day
            {
                'name': name (time zone name),
                'current_time': current time,  # форматируйте время
                'condition': condition (check the api description),
                'temp': f'temp °C',
                'wind_speed': f"{wind_speed} м/c"
            }

        """
        pass

    def get_forecast(self, lat, lon):
        """
            TODO: return a forecast for 7 days
            [{
                    'day': i,
                    'temp': sum(temps) / len(temps),  # температуры по частям дня
                    'condition': most popular condition,  # самое популярное состояние по частям дня
                    'sunrise': sunrise,
                    'sunset': sunset
            }...]
        """
        pass

