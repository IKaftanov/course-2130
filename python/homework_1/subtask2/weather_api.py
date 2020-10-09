import requests
from tokens import YANDEX_WEATHER_API_KEY, TELEGRAM_KEY

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        self.url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        self.key = api_key

    def get_current_weather(self, lat, lon):
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
        r = requests.get(self.url, data={"lat": lat, "lon": lon},
                               headers={'X-Yandex-API-Key': self.key})
        data = r.json()
        result = {
            "name": data['info']['tzinfo']['name'],
            "current_time": data['now'],
            "condition": data['fact']['condition'],
            'temp': data['fact']['temp'],
            'wind_speed': data['fact']['wind_speed']
        }
        return result

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
#weather_api = WeatherAPI(YANDEX_WEATHER_API_KEY)
#weather_api.get_current_weather(lat=55.75396, lon=37.620393)