import requests
from datetime import datetime as dt
from datetime import timedelta

class WeatherAPI:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, lat, lon):
        
        api_url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        weather = requests.get(api_url, headers={'X-Yandex-API-Key': self.api_key}).json()
        name = weather['info']['tzinfo']['name']  
        current_time = weather['now_dt']
        current_time = dt.strftime(dt.strptime(current_time[:-5], '%Y-%m-%dT%H:%M:%S') + 
                         timedelta(seconds=weather['info']['tzinfo']['offset']),
                         '%m/%d %H:%M:%S')
        condition = weather['fact']['condition']
        temp = weather['fact']['temp']
        wind_speed = weather['fact']['wind_speed']
        weather_dict =  {
                'name': name,
                'current_time': current_time,
                'condition': condition,
                'temp': f'{temp} °C',
                'wind_speed': f"{wind_speed} m/s"
                }
        msg = ''
        for key, value in weather_dict.items():
            msg += key + ': ' + str(value) + '\n'
            
        return msg

    def get_forecast(self, lat, lon):

        api_url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        weather = requests.get(api_url, headers={'X-Yandex-API-Key': self.api_key}).json()
        forecasts = []
        day = 0
        for forecast in weather['forecasts']:
            day += 1
            temps = []
            conditions = []
            for part in forecast['parts']:
                try:
                    temps.append(forecast['parts'][part]['temp_avg'])
                    conditions.append(forecast['parts'][part]['condition'])
                except KeyError:
                    pass
            cnt_base = 0
            for k in conditions:
                cnt = conditions.count(k)
                if cnt > cnt_base:
                    cnt_base = cnt
                    condition = k
            sunrise = forecast['sunrise']
            sunset = forecast['sunset']
            day_dict = {
                    'day': day,
                    'temp': sum(temps) / len(temps),
                    'condition': condition,
                    'sunrise': sunrise,
                    'sunset': sunset
                    }
            msg = ''
            for key, value in day_dict.items():
                msg += key + ': ' + str(value) + '\n'
            
            forecasts.append(msg)
            
        return '\n'.join(forecasts)