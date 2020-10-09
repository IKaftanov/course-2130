import requests
import time

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        self.api_key = api_key
        pass

    def get_current_weather(self,lat, lon):
        header = {'X-Yandex-API-Key': self.api_key }
        weather = requests.get(self.api_url.format(lat=lat, lon=lon), headers=header).json()
        name = weather['info']['tzinfo']['name']
        current_time = weather['now_dt']
        t = time.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        current_time = time.strftime("%m/%d %H:%M:%S", t)
        temp = weather['fact']['temp']
        wind_speed = weather['fact']['wind_speed']
        today = 'time zone:{0}\ncurrent_time:{1}\ntemp:{2}°C\nwind_speed:{3}M/C'.format(name, current_time, temp, wind_speed)
        return today

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

    def get_forecast(self,lat, lon):
        header = {'X-Yandex-API-Key': self.api_key}
        weather = requests.get(self.api_url.format(lat=lat, lon=lon), headers=header).json()
        forecast = ""
        partlst = ["night","morning","day","evening"]

        for i in range(7):
            temps = 0
            conds = []
            for key in partlst:
                temps += weather['forecasts'][i]['parts'][key]['temp_avg']
                conds.append(weather['forecasts'][i]['parts'][key]['condition'])
            temp = str(round(temps/4,2))
            condition = max(set(conds),key=conds.count)
            sunrise = weather['forecasts'][i]['sunrise']
            sunset = weather['forecasts'][i]['sunset']
            forecast = forecast + 'day:{0},temp:{1},condition:{2},sunrise/sunset:{3}/{4}\n'.format(i, temp, condition, sunrise, sunset)
        return forecast
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
