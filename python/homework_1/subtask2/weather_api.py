import requests


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        self.api_key = api_key
        pass

    def get_current_weather(self,lat, lon):
        lat = str(lat)
        lon = str(lon)
        api_url = 'https://api.weather.yandex.ru/v2/forecast?lat=' + lat + '&lon=' + lon + '&extra=true'
        header = {'X-Yandex-API-Key': self.api_key }
        weather = requests.get(api_url, headers=header).json()
        name = weather['info']['tzinfo']['name']
        current_time = weather['now_dt']
        import time
        t = time.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        current_time = time.strftime("%m/%d %H:%M:%S", t)
        temp = weather['fact']['temp']
        wind_speed = weather['fact']['wind_speed']
        today = 'time zone:%s\ncurrent_time:%s\ntemp:%s°C\nwind_speed:%sM/C' % (name, current_time, temp, wind_speed)
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
        lat = str(lat)
        lon = str(lon)
        api_url = 'https://api.weather.yandex.ru/v2/forecast?lat=' + lat + '&lon=' + lon + '&extra=true&limit=7'
        header = {'X-Yandex-API-Key': self.api_key}
        weather = requests.get(api_url, headers=header).json()
        forecast = ""

        def tempa(x):
            k = 0
            t = 0
            a = 0
            while k <= 23:
                try:
                    t = t + weather['forecasts'][x]['hours'][k]['temp']
                    a += 1
                except IndexError:
                    pass
                k += 1
            try:
                temp = round(t / a, 2)
            except ZeroDivisionError:
                temp = "no information"
            return temp

        def pop_condition(x):
            list = []
            for c in range(24):
                try:
                    list.append(weather['forecasts'][x]['hours'][c]['condition'])
                    conditions = max(set(list), key=list.count)
                except IndexError:
                    conditions = "no imformation"
            return conditions

        for i in range(7):
            temp = str(tempa(i))
            condition = pop_condition(i)
            sunrise = weather['forecasts'][i]['sunrise']
            sunset = weather['forecasts'][i]['sunset']
            forecast = forecast + 'day:%s,temp:%s,condition:%s,sunrise/sunset:%s/%s\n' % (
                i, temp, condition, sunrise, sunset)
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
