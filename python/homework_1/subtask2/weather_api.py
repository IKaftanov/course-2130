import requests
import datetime
from collections import Counter


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true&limit=7'

    def __init__(self, api_key):
        # Как написано в документации к API
        self.headers = { 'X-Yandex-API-Key': api_key }

    def get_current_weather(self, lat: float, lon: float) -> dict:
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
        # Предположим, что все запросы успешны, поэтому сразу просим JSON
        data = requests.get(
            self.api_url.format(lat=lat, lon=lon),
            headers=self.headers
        ).json()

        return {
            'name': data['info']['tzinfo']['name'],
            # Чтобы не заморачиваться с форматированием даты
            'current_time': datetime.datetime.fromtimestamp(data['now']).isoformat(),
            **{
                key: data['fact'][key]
                for key in 'condition temp wind_speed'.split()
            }
        }


    def get_forecast(self, lat, lon) -> list:
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
        data = requests.get(
            self.api_url.format(lat=lat, lon=lon),
            headers=self.headers
        ).json()

        parts_skipped = 'day_short', 'night_short'

        # Без дичи, ни единого моржа
        forecasts = []
        # Сортируем прогнозы по дню на всякий случай
        for day, forecast in enumerate(sorted(data['forecasts'], key=lambda fc: fc['date']), 1):
            # Получаем списки температур и эээ состояний погоды
            # для каждой части дня
            temperatures, conditions = zip(*(
                (part['temp_avg'], part['condition'])
                for name, part in forecast['parts'].items()
                if name not in parts_skipped
            ))

            one_day_forecast = {
                'day': day,
                'temp': sum(temperatures) / len(temperatures),
                'condition': Counter(conditions).most_common(1)[0][0],
                'sunrise': forecast['sunrise'],
                'sunset': forecast['sunset']
            }

            forecasts.append(one_day_forecast)

        return forecasts
