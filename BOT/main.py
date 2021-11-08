from selenium import webdriver
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='2056840015:AAGwDSl-kC4ChtIAeOlSNq2BEtRvBYeoido', use_context=True)
dispatcher = updater.dispatcher
driver = webdriver.Chrome('/Users/eugenborisenko/Desktop/POA BOT/chromedriver')


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    """ Отправляет сообщение, когда запускается /start"""

    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в бота, который выдает по тикеру информацию об акции!\n"
                                                                    "Для просмотра команд введите /help.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Список команд:\n'
                                                                    '1)/price "пробел" тикер компании; Команда для получения текущей цены. (Например, /price poly).\n'
                                                                    '2)/cap "пробел" тикер компании; Команда для получения капитализации компании. (Например, /cap gazp).')
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def price(update, context):
    ticker = ' '.join(context.args).upper()
    url = f"https://www.moex.com/ru/issue.aspx?board=TQBR&code={ticker}"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price = soup.find(class_='last')
    if price is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Такого тикера нет.')
        return
    price = price.get_text()
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(price) + ' рублей')

price_handler = CommandHandler('price', price)
dispatcher.add_handler(price_handler)

def cap(update, context):
    ticker = ' '.join(context.args).upper()
    url = f"https://www.moex.com/ru/issue.aspx?board=TQBR&code={ticker}"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    span_cap = soup.select_one("span[title*=капитализация]")
    if span_cap is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Такого тикера нет.')
        return
    cap = span_cap.get_text()[15:].replace(" ","")
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(cap) + ' рублей')

cap_handler = CommandHandler('cap', cap)
dispatcher.add_handler(cap_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Такой команды нет.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)