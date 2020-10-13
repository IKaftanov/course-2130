import requests

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example
    api_key = {}
    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
    response = requests.get(api_url, headers=api_key)
    data = response.json()
    fact = data['fact']
    info = data['info']
    forecasts = data['forecasts']
    dt_now = datetime.now()

    def __init__(self, api_key):
        pass

    def get_current_weather(self, lat, lon):

        print(dt_now.strftime('%d.%m.%Y %H:%M'))
        print('time zone name', info['tzinfo']["name"])
        print('description :', fact['condition'])
        print('Temperature :', fact['temp'], 'degrees Celsius')
        print('Wind speed:', fact['wind_speed'], 'm/s')

        pass

    def get_forecast(self, lat, lon):
        for i in range(0, 7):
            print('Date:', forecasts[i]["date"])
            t1 = forecasts[i]["parts"]["night"]["temp_avg"]
            t2 = forecasts[i]["parts"]["day"]["temp_avg"]
            t3 = forecasts[i]["parts"]["morning"]["temp_avg"]
            t4 = forecasts[i]["parts"]["evening"]["temp_avg"]
            print("average temp:", (t1 + t2 + t3 + t4) / 4)

            print('night condition', forecasts[i]["parts"]["night"]["condition"])
            print('morning condition', forecasts[i]["parts"]["morning"]["condition"])
            print('day condition', forecasts[i]["parts"]["day"]["condition"])
            print('evening condition', forecasts[i]["parts"]["evening"]["condition"])
            print('sunrise:', forecasts[i]["sunrise"])
            print('sunset:', forecasts[i]["sunset"])

        pass