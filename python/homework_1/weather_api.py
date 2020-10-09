import requests
from datetime import datetime
from collections import Counter


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example


    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

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
        request = requests.get(self.api_url, data={'lat': lat, 'lon': lon},
                               headers={'X-Yandex-API-Key': self.api_key}).json()
        cur_weather = {'name': request['info']['tzinfo']['name'],
                       'current_time': datetime.fromtimestamp(int(request['now'])).strftime('%Y-%m-%d | %H:%M:%S'),
                       'condition': request['fact']['condition'], 'temp': str(request['fact']['temp']) + ' \u00b0C',
                       'wind speed': str(request['fact']['wind_speed']) + ' m/s'}
        return cur_weather

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
        request = requests.get(self.api_url, data={'lat': lat, 'lon': lon},
                               headers={'X-Yandex-API-Key': self.api_key}).json()
        day_parts = ['night', 'morning', 'day', 'evening']
        forecasts = [{'day': day['date'],
                      'temp': str(sum([day['parts'][part]['temp_avg'] for part in day_parts]) / 4) + ' \u00b0C',
                      'condition': Counter([day['parts'][part]['condition'] for part in day_parts]).most_common(1)[0][
                          0],
                      'sunrise': day['sunrise'],
                      'sunset': day['sunset'],
                      }
                     for i, day in enumerate(request['forecasts'])]
        return forecasts
