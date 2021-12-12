import telebot
from telebot import types
bot = telebot.TeleBot("2105927185:AAHt27CwgQ2Rsaek0VLdvonsl09BY4ztp6k")

name = ''
age = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello,How are you?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Hello':
        bot.reply_to(message, 'Hello, Have a nice day!')
    elif message.text == 'Hi':
        bot.reply_to(message, 'Hi!')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "hello, What your name? Nice to meet you!")
        bot.register_next_step_handler(message, reg_age)
    bot.reply_to(message, message.text)
def reg_age(message):
    global age
    age = message.text
    bot.send_message(message.from_user.id, "hello, How old are you? ")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global reg_age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Enter the numbers !")

        keyboard = types.InLineKeyboardMarkup
        key_yes = types.InLineKeyboardMarkup(text = 'yes')
        keyboard.add(key_yes)
        key_no = types.InLineKeyboardMarkup(text = 'no')
        keyboard.add(key_no)
        question = 'You' + str(age) + 'old?'
        bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Nice to meet you!, Now write something.")
    elif call.data == "no":
        bot.send_message(call.massage.chat.id, "Try again!")
        bot.send_message(call.message.chat.id, "Nice to meet you!")
        bot.register_next_step_handler(call.message, reg_age)



bot.polling()