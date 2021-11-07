# Короткое имя бота @yfin_bot

import telebot
import yfinance as yf
import plotly.graph_objects as go

token = '2081072252:AAGNY1EmlUknXfH6iMZn2xD--xSA1pSZrCs'
bot = telebot.TeleBot(token)

ticker = '';
freq = {"1d":("1 день","1h"),
        "1mo":("1 месяц","1d"),
        "6mo":("6 месяцев","1wk"),
        "1y":("1 год","1wk"),
        "5y":("5 лет","1mo"),
        "max":("MAX","1mo")}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Напиши тикер");
    
@bot.message_handler(commands=['help'])
def start_message(message):
    s = ("Привет! Я бот. Выбери компанию, запиши ее тикер и выбери период времени, "
         "за который я выведу динамику котировок ее акций.")
    bot.send_message(message.from_user.id, s);

@bot.message_handler(content_types=['text'])
def get_ticker(message):
    global ticker;
    ticker = message.text
    if yf.Ticker(ticker).info['regularMarketPrice'] == None:
        bot.send_message(message.from_user.id, 'Нет такого тикера');
        bot.register_next_step_handler(message, get_ticker);
    else :
        markup = telebot.types.InlineKeyboardMarkup()
        for k, v in freq.items():
            markup.add(telebot.types.InlineKeyboardButton(text=v[0], callback_data=k))
        bot.send_message(message.chat.id, text="Выбери период", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global ticker;
    global freq;    
    bot.answer_callback_query(callback_query_id=call.id, text='Thanks');    
    data = yf.download(tickers = ticker,period = call.data,interval = freq[call.data][1]);
    
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.write_image("fig.png")
    
    bot.send_photo(call.message.chat.id, open('fig.png', 'rb'));    
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id);

bot.polling(none_stop=True, interval=0)