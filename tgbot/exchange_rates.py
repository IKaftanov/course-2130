import requests
import json
from config import URL


class ExchangeRatesLoader:

    def __init__(self):
        self.data = json.loads(requests.get(URL).text)

    def get_exchange_rate(self, currency_key):  # возвращает курс по запрошенной валюте
        data = self.data["Valute"]
        date = self.data["Date"][:10]
        new_date_format = date[8:19] + '.' + date[5:7] + '.' + date[:4]
        for currency in data:
            if currency == currency_key:
                value = round(data[currency]["Value"] / data[currency]["Nominal"], 2)
                previous = round(data[currency]["Previous"] / data[currency]["Nominal"], 2)
                change = round(value - previous, 2)
                return str(f'По официальному курсу ЦБ РФ на {new_date_format}\n'
                           f'{data[currency]["CharCode"]} = {value} RUB\n'
                           f'-------------------------------\n'
                           f'Предыдущее значение: {data[currency]["CharCode"]} = {previous} RUB\n'
                           f'Изменение: {change}')
            else:
                continue

    def get_dict_of_currencies(self):  # возвращает словарь, где keys - коды валют, items - названия валют
        currencies = {}
        data = self.data["Valute"]
        for currency in data:
            c_name = data[currency]["Name"].split()

            if c_name[0][len(c_name[0]) - 2:] == 'их' and c_name[1][len(c_name[1]) - 2:] == 'ов':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ий'
                c_name[1] = c_name[1][:len(c_name[1]) - 2]

            elif c_name[0][len(c_name[0]) - 2:] == 'их' and c_name[1] == 'крон':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ая'
                c_name[1] = 'крона'

            elif c_name[0][len(c_name[0]) - 2:] == 'их' and c_name[1][len(c_name[1]) - 2:] == 'ий':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ая'
                c_name[1] = c_name[1][:len(c_name[1]) - 2] + 'ия'

            elif c_name[0][len(c_name[0]) - 2:] == 'их' and c_name[1][len(c_name[1]) - 2:] == 'ев':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ий'
                c_name[1] = c_name[1][:len(c_name[1]) - 2] + 'й'

            elif c_name[0][len(c_name[0]) - 2:] == 'их' and len(c_name[1]) == 3:
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ая'
                c_name[1] = c_name[1] + 'а'

            elif c_name[0][len(c_name[0]) - 2:] == 'их' and c_name[1][len(c_name[1]) - 2:] == 'ен':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ая'
                c_name[1] = c_name[1][:len(c_name[1]) - 2] + 'на'

            elif c_name[0][len(c_name[0]) - 2:] == 'их':
                c_name[0] = c_name[0][:len(c_name[0]) - 2] + 'ий'

            else:
                pass

            new_currency_name = ' '.join(c_name)
            currencies[data[currency]["CharCode"]] = new_currency_name
        return currencies

    def print_available_currencies(self):
        currencies = self.get_dict_of_currencies()
        currencies_string = 'Список доступных валют:\n'
        for key in currencies:
            string = f'{key}:\t{currencies[key]}\n'
            currencies_string = currencies_string + string
        return currencies_string

    def convert_to_foreign(self, currency_key, amount_in_rub):
        data = self.data["Valute"]
        amount_in_rub = float(amount_in_rub)
        exchange_rate = float(data[currency_key]["Value"]) / int(data[currency_key]["Nominal"])
        amount_in_foreign_currency = round(amount_in_rub / exchange_rate, 2)
        return str(f'{amount_in_rub} RUB = {amount_in_foreign_currency} {data[currency_key]["CharCode"]}')

    def convert_to_rub(self, currency_key, amount_in_foreign):
        data = self.data["Valute"]
        amount_in_foreign = float(amount_in_foreign)
        exchange_rate = float(data[currency_key]["Value"]) / int(data[currency_key]["Nominal"])
        amount_in_rub = round(amount_in_foreign * exchange_rate, 2)
        return str(f'{amount_in_foreign} {data[currency_key]["CharCode"]} = {amount_in_rub} RUB')
