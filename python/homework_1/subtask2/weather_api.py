import requests
import datetime as dt
import collections as coll

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    def __init__(self, api_key):
        self.url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        self.key = api_key

    def get_current_weather(self, lat, lon):
        response = requests.get(self.url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.key}).json()
        current = {'time zone': response['info']['tzinfo']['name'],
                    'current time': dt.datetime.fromtimestamp(response['now']).strftime('%m-%d %H:%M:%S'),
                    'condition': response['fact']['condition'],
                    'temp': '{temp} °C'.format(temp = response['fact']['temp']),
                    'wind speed': '{wind_speed} м/с'.format(wind_speed = response['fact']['wind_speed'])}
        return ' \n'.join(f'{key}: {value}' for key, value in current.items())


    def get_forecast(self, lat, lon):
        response = requests.get(self.url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.key}).json()
        string = ''

        def average_temperature(parts):
            first = (parts['day']['temp_avg'] + parts['night']['temp_avg'])/4
            second = (parts['evening']['temp_avg']+parts['morning']['temp_avg'])/4
            return first+second

        def most_popular_condition(parts):
            conditions = (parts['day']['condition'],parts['night']['condition'],parts['evening']['condition'], parts['morning']['condition'])
            return coll.Counter(conditions).most_common(1)[0][0]

        def forecast_weather(ind, day):
            forecast = {'day': ind,
                     'temp': '{temp} °C'.format(temp = average_temperature(day['parts'])),
                     'condition': most_popular_condition(day['parts']),
                     'sunrise/sunset': '{sunrise}/{sunset}'.format(sunrise = day['sunrise'], sunset = day['sunset'])}
            return ', '.join(f'{key}: {value}' for key, value in forecast.items())

        for ind, day in enumerate(response['forecasts']):
            string += '\n\n' + forecast_weather(ind, day)
        return string



