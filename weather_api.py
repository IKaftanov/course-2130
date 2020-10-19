import requests
from datetime import datetime
from collections import Counter

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
        pass

    def get_current_weather(self, lat, lon):
        
        res = requests.get(self.api_url, data={"lat": lat, "lon": lon}, 
                               headers={'X-Yandex-API-Key': self.api_key}).json()
        weather_now = {'time_zone': res['info']['tzinfo']['name'],
                   'current_time': datetime.fromtimestamp(int(res['now'])).strftime('%Y-%m-%d %H:%M:%S'),
                   'condition': res['fact']['condition'],
                   'temp': str(res['fact']['temp'])+ ' \u00b0C',
                   'wind_speed': str(res['fact']['wind_speed'])+' м/c'
                }
        return weather_now    
       
    def get_forecast(self, lat, lon):
        
        res = requests.get(self.api_url, data={'lat': lat, 'lon': lon},
                               headers={'X-Yandex-API-Key': self.api_key}).json()
        day_parts = ['night', 'morning', 'day', 'evening']
        forecast = [{'day': day['date'],
                      'temp': str(sum([day['parts'][part]['temp_avg'] for part in day_parts]) / 4) + ' \u00b0C',
                      'condition': Counter([day['parts'][part]['condition'] for part in day_parts]).most_common(1)[0][
                          0],
                      'sunrise': day['sunrise'],
                      'sunset': day['sunset'],
                      }
                     for i, day in enumerate(res['forecasts'])]
        return forecast