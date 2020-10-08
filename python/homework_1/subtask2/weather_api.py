import requests
from datetime import datetime


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example
    # ключ 3deab848-6121-4fba-808d-d3d342ad0776

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        self.api_key = api_key

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
        # print(self.api_url.format(lat=lat, lon=lon))
        response = requests.get(self.api_url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.api_key})

        if (response.status_code != 200):
            return 'Error get current weather from API'

        weather = response.json()
        time_zone = weather['info']['tzinfo']['name']
        current_time = weather['now']
        current_time = datetime.fromtimestamp(current_time).strftime("%A, %B %d, %Y %I:%M:%S")
        condition = weather['fact']['condition']
        temp = weather['fact']['temp']
        wind_speed = weather['fact']['wind_speed']
        return 'Часовой пояс: {}\nДата и время: {}\nПогодные условия: {}' \
               '\nТемпература воздуха: {}°C\nСкорость ветра: {} м/c\n'.format(time_zone, current_time, condition, temp, wind_speed)

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
        response = requests.get(self.api_url.format(lat=lat, lon=lon), headers={'X-Yandex-API-Key': self.api_key})

        if (response.status_code != 200):
            return 'Error get current weather from API'

        weather = response.json()
        forecast = weather['forecasts']
        day_weather = 'day: {}, temp: {}, condition: {}, sunrise/sunset: {}/{}'

        message = []
        for i, day in enumerate(forecast):
            # print(day)
            sunrise = day['sunrise']
            sunset = day['sunset']
            temp = (day['parts']['day_short']['temp'] + day['parts']['night_short']['temp']) / 2
            conditions = []
            for key in day['parts']:
                conditions.append(day['parts'][key]['condition'])
            condition = ''
            con_count = 0
            for item in set(conditions):
                cur_count = conditions.count(item)
                if cur_count > con_count:
                    condition = item
                    con_count = cur_count

            message.append(day_weather.format(i, temp, condition, sunrise, sunset))

        return "\n".join(message)

