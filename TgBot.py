import telebot
token = '2138375880:AAFwIiq492CNkBUqHLowp6UDEIzvsGQH15A'

bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def message_received(message):
    if message.text == 'Привет':
        bot.send_message(chat_id=message.from_user.id, text=fr'Ну привет, {message.from_user.username}')
    elif message.text == 'Пока':
        bot.send_message(chat_id=message.from_user.id, text='Не очень то и хотелось')
    elif message.text == 'Я тебя люблю':
        bot.send_message(chat_id=message.from_user.id, text='Все меня любят')
    elif message.text == 'Как дела?':
        bot.send_message(chat_id=message.from_user.id, text='Все тлен')
    else:
        bot.send_message(chat_id=message.from_user.id, text=message.text)


bot.polling(True)