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

        # Возвращаем список из словарей,
        # по одному словарю для каждого дня.
        # Это одно большое выражение.
        return [
            # Это тьюпл, первые три элемента которого - просто
            # для расчётов, а последний включается в результат
            (
                # Используем оператор-морж (walrus operator) для присвоения внутри выражения
                parts := [
                    (part['temp_avg'], part['condition'])
                    for name, part in forecast['parts'].items()
                    if name not in parts_skipped
                ],
                temps := [temp for temp, _ in parts],
                conds := (cond for _, cond in parts), # Это ленивая операция
                {
                    'day': day,
                    # Вся дичь с моржами нужна фактически только для того,
                    # чтобы здесь получилось красивое вычисление среднего,
                    # а также Counter(conds)
                    'temp': sum(temps) / len(temps),
                    'condition': Counter(conds).most_common(1)[0][0],
                    'sunrise': forecast['sunrise'],
                    'sunset': forecast['sunset']
                }
            )[-1]
            for day, forecast in enumerate(sorted(data['forecasts'], key=lambda fc: fc['date']), 1)
        ]

if __name__ == '__main__':
    # For testing only

    from tokens import YANDEX_WEATHER_API_KEY
    LOC = {'longitude': 37.3, 'latitude': 55.1}

    api = WeatherAPI(YANDEX_WEATHER_API_KEY)
    print(api.get_forecast(LOC['latitude'], LOC['longitude']))
