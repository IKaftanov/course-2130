import logging

import telegram
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

from weather_api import WeatherAPI
from tokens import YANDEX_WEATHER_API_KEY, TELEGRAM_KEY

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


WEATHER_CONVERSATION_COMMANDS = ['current', 'forecast']
WEATHER_COMMAND_SELECTION = 0
WEATHER_RETURN = 1


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    
    update.message.reply_text('Welcome to my weather API bot')


def get_weather_start(update, context):
    reply_markup = ReplyKeyboardMarkup([[KeyboardButton('send my location', request_location=True)]])
    update.message.reply_text('Send me the coordinates or /cancel', reply_markup=reply_markup)
    return 0


def coordinates_handler(update, context):
    reply_markup = ReplyKeyboardMarkup(
        [[KeyboardButton(item) for item in WEATHER_CONVERSATION_COMMANDS]]
    )

    context.user_data["location"] = update.message.location
    update.message.reply_text(
        'Thank you. You location {} is captured'.format(context.user_data["location"]),
        reply_markup=reply_markup
    )
    return 1


def weather_handler(update: Update, context: CallbackContext):
    if update.message.text == WEATHER_CONVERSATION_COMMANDS[0]:
        loc = context.user_data['location']
        reply = weather_api.get_current_weather(loc['latitude'], loc['longitude'])
        
        update.message.reply_text('''
Current weather for {name}, time: {current_time}:

Condition: {condition}
Temperature: {temp} °C
Wind speed: {wind_speed} m/s
        '''.strip().format(**reply))
    elif update.message.text == WEATHER_CONVERSATION_COMMANDS[1]:
        loc = context.user_data['location']
        reply = weather_api.get_forecast(loc['latitude'], loc['longitude'])

        for day in reply:
            update.message.reply_text('''
Day {day}:
    Condition: {condition}
    Avg temperature: {temp} °C
    Sunrise at {sunrise}
    Sunset at {sunset}
            '''.strip().format(**day))

    update.message.reply_text("This is it!", reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Ok, thank you for your attention!', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start_telegram_bot():
    updater = Updater(TELEGRAM_KEY, use_context=True)
    dp = updater.dispatcher
    # setup commands
    dp.add_handler(CommandHandler("start", start))

    event_conversation = ConversationHandler(
        entry_points=[CommandHandler("weather", get_weather_start)],
        states={
            0: [MessageHandler(Filters.location, coordinates_handler)],
            1: [MessageHandler(Filters.regex(f'^({"|".join(WEATHER_CONVERSATION_COMMANDS)})'), weather_handler)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dp.add_handler(event_conversation)
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    weather_api = WeatherAPI(YANDEX_WEATHER_API_KEY)
    start_telegram_bot()
