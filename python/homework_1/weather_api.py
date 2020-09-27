import requests


class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example

    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'

    def __init__(self, api_key):
        pass

    def _get_weather(self, lat=55.75396, lon=37.620393):
        pass

    def get_current_weather(self, lat, lon):
        """
            TODO: return a weather in readable format
            The returned data must contains:
            | name (time zone name)  | current time  | condition (check the api description) | temp | wind_speed
        """
        pass

    def get_forecast(self, lat, lon):
        """
            TODO: return a forecast for 7 days
            | day | name (time zone) | avg by hours | sunrise | sunset | is rainy? |
            | day ................................................................ |
            .......................................................................
            | day7 ................................................................|
        """
        pass