import requests

import datetime as dt
import collections as coll

class WeatherAPI:

	 # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example
	 

	def __init__(self, api_key):
		
		self.url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
		self.key = api_key

	def get_current_weather(self, lat, lon):

		data = requests.get(self.url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.key}).json()
		
		current_weather = { 'time zone': data['info']['tzinfo']['name'],
						   'current time': dt.datetime.fromtimestamp(data['now']).strftime('%m-%d %H:%M:%S'),
						   'condition': data['fact']['condition'],
						   'temp': '{temp} °C'.format(temp = data['fact']['temp']),
						   'wind speed': '{wind_speed} м/c'.format(wind_speed = data['fact']['wind_speed']) }

		return ' \n'.join(f'{k}: {v}' for k, v in current_weather.items())

		
	def get_forecast(self, lat, lon):

		data = requests.get(self.url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.key}).json()

		def avg_part(parts):
			sum = parts['day']['temp_avg']+parts['night']['temp_avg']+parts['evening']['temp_avg']+parts['morning']['temp_avg']
			return sum/4
			
		def mostCommon(parts):
			lst = [parts['day']['condition'],parts['night']['condition'],parts['evening']['condition'],parts['morning']['condition']]
			return coll.Counter(lst).most_common(1)[0][0]
	
		def forecast(ind, day):
			pred = { 'day': ind,
                    'temp': '{temp} °C'.format(temp = avg_part(day['parts'])),  # температуры по частям дня
                    'condition': mostCommon(day['parts']),  # самое популярное состояние по частям дня
                    'sunrise/sunset': '{r}/{s}'.format(r = day['sunrise'], s = day['sunset']) }
			return ', '.join(f'{k}: {v}' for k, v in pred.items())

		res = ''
		for ind, day in enumerate(data['forecasts']):
			res = res +'\n\n' + forecast(ind ,day)

		return res