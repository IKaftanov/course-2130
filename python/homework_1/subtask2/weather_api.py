import requests

import datetime as dt
from collections import Counter

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def get_current_weather(self, lat, lon):
        response = requests.get(self.api_url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.api_key}).json()

        temp = response['fact']['temp']
        wind_speed = response['fact']['wind_speed']

        weather_dictionary = {'time zone': response['info']['tzinfo']['name'],
                              'current time': dt.datetime.fromtimestamp(response['now']).strftime('%m/%d %H:%M:%S'),
                              'condition': response['fact']['condition'],
                              'temp': f'{temp} °C',
                              'wind speed': f'{wind_speed} m/s'}

        return ' \n'.join(f'{key}: {value}' for key, value in weather_dictionary.items())


    def get_forecast(self, lat, lon):
        response = requests.get(self.api_url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.api_key}).json()
        bot_answer = ''

        def avg_temp(parts):
            sum_temps = (parts['day']['temp_avg'] + parts['night']['temp_avg'] +
                         parts['evening']['temp_avg'] + parts['morning']['temp_avg'])
            return sum_temps / 4

        def most_popular_condition(parts):
            most_popular = [parts['day']['condition'], parts['night']['condition'], parts['evening']['condition'],
                            parts['morning']['condition']]
            count = Counter(most_popular)
            return count.most_common()[0][0]

        def forecast(i, day):
            r = day['sunrise']
            s = day['sunset']
            temp = avg_temp(day['parts'])
            prediction = {'day': i,
                    'temp': f'{temp} °C',
                    'condition': most_popular_condition(day['parts']),
                    'sunrise/sunset': f'{r}/{s}'}
            return ', '.join(f'{key}: {value}' for key, value in prediction.items())

        for i, day in enumerate(response['forecasts']):
            bot_answer = bot_answer + '\n\n' + forecast(i, day)

        return bot_answer