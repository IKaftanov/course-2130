import logging
import telegram
from telegram import Update
import json
from math import cos, asin, sqrt
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, 
                          ConversationHandler, CallbackContext)

# bot: https://t.me/nearest_restaurant_bot

TELEGRAM_KEY = '2052182860:AAGGiPO5uZ-6hQUKj7HAFSIr-Hz8sQH1EGw'

RESTAURANTS_CONVERSATION_COMMANDS = ['nearest', 'add']
RESTAURANTS_COMMAND_SELECTION, RESTAURANTS_RETURN, NAME , LONGITUDE, LATITUDE, ADRESS = range(0, 6)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)    
    
# ---------- location hadling functions ---------
    
def get_district(lng,lat):
    lng  = float(lng)
    lat = float(lat)
    if ((lng > 55.91) | (lng < 55.57) | (lat > 37.84) | (lng < 37.35)):
        return 'You are not in Moscow'
    else:
        if lng > 55.76:
            if lat > 37.59:
                if lng > 0.6*lat:
                    return 'A'
                else:
                    return 'B'
            else:
                if lng > -0.6*lat:
                    return 'H'
                else:
                    return 'G'
                
        else:
            if lat > 37.59:
                if lng > -0.6*lat:
                    return 'C'
                else:
                    return 'D'
            else:
                if lng > 0.6*lat:
                    return 'F'
                else:
                    return 'E'               


# Haversine formula
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, lng,lat):
    return min(data, key=lambda p: distance(float(lat),float(lng),float(p['latitude']),float(p['longitude'])))


def return_rest(lng,lat):
    with open('data.txt', 'r') as outfile:
        input_dict = json.load(outfile)
    output_dict = [x for x in input_dict if x['district'] == get_district(lng,lat)]
    return closest(output_dict, lng, lat)

def add_rest(rest):
    with open('data.txt', 'r') as outfile:
        input_dict = json.load(outfile)
    input_dict.append(rest)
    with open('data.txt', 'w') as outfile1:
        json.dump(input_dict, outfile1) 
        
        



# ---------- bot functions ---------

def got_name(update: Update, context: CallbackContext):
    name = update.message.text # now we got the name
    context.user_data["name"] = name # to use it later (in next func)
    text = f"Thanks for adding name {name} ! Now send me it's longitude"
    update.message.reply_text(text)
    return 3

def got_longitude(update: Update, context: CallbackContext):
    longitude = update.message.text # now we got the longitude
    context.user_data["longitude"] = longitude # to use it later (in next func)
    text = f"Thanks for adding longitude: {longitude} ! Now send me it's latitude"
    update.message.reply_text(text)
    return 4

def got_latitude(update: Update, context: CallbackContext):
    latitude = update.message.text # now we got the latitude
    context.user_data["latitude"] = latitude # to use it later (in next func)
    text = f"Thanks for adding latitude: {latitude} ! We almost finished! Tell me it's adress"
    update.message.reply_text(text)
    return 5

def got_adress(update: Update, context: CallbackContext):
    adress = update.message.text # now we got the adress
    context.user_data["adress"] = adress # to use it later (in next func)
    text = f"Thanks for adding adress: {adress} ! Rate the restaurant from 1 to 5."
    update.message.reply_text(text)
    return 6

def got_rating(update: Update, context: CallbackContext):
    rating = update.message.text # now we got the rating
    context.user_data["rating"] = rating # to use it later (in next func)
    k=0
    try:
        district = get_district(context.user_data["latitude"], context.user_data["longitude"])
    except Exception as e:
        district = 'Error'
        k=1
        
    with open('data.txt', 'r') as outfile:
        idshnik = len(json.load(outfile))
    
    restik = {'id': idshnik,
     'name': context.user_data["name"],
     'adress': context.user_data["adress"],
     'district': district,
     'longitude': context.user_data["latitude"],
     'latitude': context.user_data["longitude"],
     'rating': context.user_data["rating"]}
    
    # add new restaurant
    if k ==0:
        add_rest(restik)
        text = "Thanks! Restaurant added successfully!!!"
        update.message.reply_text(text)
    else:
        update.message.reply_text('Something went wrong. Coordinates should be numeric!')
    
    return ConversationHandler.END



def start(update, context):
    """Send a message when the command /start is issued."""

    update.message.reply_text("Welcome to Restaurant Recomendation Bot. I'll help you to find the best restaurant near you! \n/restaurants -- get nearest restaurant in Moscow or add a new one! \n/help -- if you need some")

def restaurants_start(update, context):
    reply_markup = telegram.ReplyKeyboardMarkup([[telegram.KeyboardButton('send my location', 
                                                                          request_location=True)]])
    update.message.reply_text('Send me the coordinates or /cancel', reply_markup=reply_markup)
    return 0

def coordinates_handler(update, context):
    reply_markup = telegram.ReplyKeyboardMarkup(
        [[telegram.KeyboardButton(item) for item in RESTAURANTS_CONVERSATION_COMMANDS]]
    )
    update.message.reply_text('Thank you. Your location is captured. \n Select "nearest" to get the closest restaurant or select "add" to extend the database!', reply_markup=reply_markup)
    # find and save location property in update
    # you can use `context.user_data["location"]` to save user data
    context.user_data["location"] = update.message.location
    return 1



def restaurant_handler(update, context):
    long = context.user_data["location"]['latitude']
    lati = context.user_data["location"]['longitude']
      
    if update.message.text == RESTAURANTS_CONVERSATION_COMMANDS[0]:
        update.message.reply_text('Want to find a nearest restaurant? Let me search...', reply_markup=telegram.ReplyKeyboardRemove())
        # return nearest restaurant location
        rest_reply = return_rest(lng=long,lat=lati)
        
        update.message.reply_text(f"The nearest restaurant is {rest_reply['name']}! \nIt's adress is {rest_reply['adress']}. \nCould be found in district {rest_reply['district']} and rated {rest_reply['rating']}/5 by users")
    elif update.message.text == RESTAURANTS_CONVERSATION_COMMANDS[1]:
        update.message.reply_text(text = "Want to add a restaurant? Please, type it's name first!", reply_markup=telegram.ReplyKeyboardRemove())
        return 2
        
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Ok, thank you for your attention!', reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def help_handler(update: Update, context: CallbackContext) -> None:
    """Display a help message"""
    update.message.reply_text("""List of commands:
    /start - begin conversation
    /restaurants - find a restaurant or add one 
    /cancel - cancel operation 
    /help - what to do?""")

    
def start_telegram_bot():
    updater = Updater(TELEGRAM_KEY, use_context=True)
    dp = updater.dispatcher
    # setup commands
    dp.add_handler(CommandHandler("start", start))

    event_conversation = ConversationHandler(
        entry_points=[CommandHandler("restaurants", restaurants_start)],
        states={
        0 : [MessageHandler(Filters.location, coordinates_handler)],
        1 : [MessageHandler(Filters.regex(f'^({"|".join(RESTAURANTS_CONVERSATION_COMMANDS)})'), restaurant_handler)],
        2 : [MessageHandler(Filters.text , got_name)],
        3 : [MessageHandler(Filters.text , got_longitude)],
        4 : [MessageHandler(Filters.text , got_latitude)],
        5 : [MessageHandler(Filters.text , got_adress)],
        6 : [MessageHandler(Filters.text , got_rating)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dp.add_handler(event_conversation)
    dp.add_error_handler(error)
    dp.add_handler(CommandHandler('help', help_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    start_telegram_bot()
