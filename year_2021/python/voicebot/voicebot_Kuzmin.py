from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os
import speech_recognition as sr

updater = Updater(token='2094428756:AAENlsaMdHOTLY9etJhcUnJnNHYLmSC7UW0')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Текст сила, гс могила')


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Я автоматически перевожу голосовые на русском языке')


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Я не понимаю, чего вы хотите')


def voice_replier(update: Update, context):
    message = update.message.voice.get_file()
    user = update.message.from_user
    message.download('voice.ogg')
    os.system('ffmpeg -loglevel warning -y -i voice.ogg voice.wav')
    file = 'C:/Users/Admin/PycharmProjects/MyBot/voice.wav'
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language='ru')
        except:
            text = 'Я не смог распознать текст'
        print(user['last_name'], user['first_name'], ': ', text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             reply_to_message_id=update.effective_message.message_id)


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
unknown_handler = MessageHandler(Filters.command, unknown)
voice_decoder_handler = MessageHandler(Filters.voice, voice_replier)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(voice_decoder_handler)

updater.start_polling()
