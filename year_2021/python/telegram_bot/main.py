from telegram import Update, ReplyKeyboardMarkup, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, Filters
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, CallbackQueryHandler

from datetime import time
import pytz
import re

import logging

from config import bot_token
import myparcer

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list={'url': {}, 'name': {}, 'status': {},
                                                                            'latest_date': {},
                                                                            'latest_chapter_name': {}})

    reply_keyboard = [['/add', '/delete'], ['/favorites', '/predict'], ['/set_notifications', '/help']]

    update.message.reply_text(text=fr'Привет {update.effective_user.first_name}!'
                              '\nЭто бот, который может отслеживать обновления манги и делать прогноз '
                              'на будущую дату выхода новой главы.'
                              '\nЧтобы разобраться в командах бота нажмите /help',
                              reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard,
                                                               one_time_keyboard=False,
                                                               input_field_placeholder='Выберите действие'))


def help_(update: Update, context: CallbackContext):
    update.message.reply_text(text='Команды: '
                              '\n1) <i>/add</i> - добавляет мангу в избранное ✅'
                              '\n2) <i>/delete</i> - удаляет мангу из избранного ❌'
                              '\n3) <i>/favorites</i> - избранное ❤'
                              '\n4) <i>/predict</i> - прогноз даты выхода следующей главы тайтла из избранного🔮'
                              '\n5) <i>/set_notifications</i> - установить уведомления об обновлениях ⏰',
                              parse_mode=ParseMode.HTML)


ADD = 1


def add(update: Update, context: CallbackContext):
    update.message.reply_text('Скиньте в чат ссылку на мангу, которую хотите добавить в избранное \n \n'
                              'Пример: \n'
                              'https://mangalib.me/bungou-stray-dogs?section=chapters')
    return ADD


def add_v2(update: Update, context: CallbackContext):
    url = update.message.text
    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    update.message.reply_text(myparcer.add_manga(url=url, manga_list=manga_list))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)
    return ConversationHandler.END


def add_cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


DEL = 3


def delete(update: Update, context: CallbackContext):
    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)

    keyboard = [[InlineKeyboardButton(i, callback_data=i)] for i in manga_list['url'].keys()]
    update.message.reply_text(text='Какую мангу вы хотите удалить из избранного?',
                              reply_markup=InlineKeyboardMarkup(keyboard))
    return DEL


def delete_v2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    name = query.data

    name = query.data
    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    query.bot.send_message(chat_id=query.message.chat_id,
                           text=myparcer.delete_manga(name=name, manga_list=manga_list))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)
    return ConversationHandler.END


def delete_cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


def favorites(update: Update, context: CallbackContext):
    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    update.message.reply_text('\n'.join(myparcer.favorites(manga_list=manga_list)))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)


def notification(context: CallbackContext):
    manga_list = myparcer.load_json(file_name=str(context.job.context[1]))
    new_chapters_list = myparcer.new_chapters_list(manga_list)
    myparcer.save_json(file_name=str(context.job.context[1]), manga_list=manga_list)

    if len(new_chapters_list) == 0:
        context.bot.send_message(chat_id=context.job.context[0],
                                 text='Новых глав нет😥')

    else:
        context.bot.send_message(chat_id=context.job.context[0],
                                 text='Вышли новые главы: \n' + '\n'.join(new_chapters_list))
        context.bot.send_animation(chat_id=context.job.context[0],
                                   animation='https://i.pinimg.com/originals/df/e2/61'
                                             '/dfe2616671565bd2e8b65197f85fc0fc.gif')


TIME = 2


def set_notifications(update: Update, context: CallbackContext):
    update.message.reply_text('В какое время вы хотите ежедневно получать уведомления⏰?\n'
                              'Пример: \n'
                              '12:5')
    return TIME


def set_notifications_v2(update: Update, context: CallbackContext):
    time_ = update.message.text
    if re.compile('^[1-2]?[0-9]:[1-5]?[0-9]$').match(time_):
        update.message.reply_text(text=fr'Ежедневное напоминание о выходе манги будет приходить в {time_}')
        context.job_queue.run_daily(notification, context=(update.message.chat_id, update.effective_user.id),
                                    time=time(hour=int(time_.split(':')[0]),
                                              minute=int(time_.split(':')[1]),
                                              tzinfo=pytz.timezone("Europe/Moscow")))
    else:
        update.message.reply_text(text='Неверный формат времени. Следует написать, например: \n'
                                       '/set_notifications 18:7')
    return ConversationHandler.END


def set_notifications_cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


PRED = 5


def predict(update: Update, context: CallbackContext):
    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)

    keyboard = [[InlineKeyboardButton(i, callback_data=i)] for i in manga_list['url'].keys()]
    update.message.reply_text(text='Дату выхода новой главы какого тайтла вы хотите предсказать?',
                              reply_markup=InlineKeyboardMarkup(keyboard))
    return PRED


def predict_v2(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    name = query.data

    manga_list = myparcer.load_json(file_name=str(update.effective_user.id))
    myparcer.save_json(file_name=str(update.effective_user.id), manga_list=manga_list)

    query.bot.send_message(chat_id=query.message.chat_id,
                           text='Вычисляю предсказание...')
    query.bot.send_animation(chat_id=query.message.chat_id,
                             animation='https://i.pinimg.com/originals/8f/0b/5b/8f0b5b1235851fbf248d32dc0a97963f.gif')
    query.bot.send_message(chat_id=query.message.chat_id,
                           text=myparcer.predict(name=name, manga_list=manga_list))
    return ConversationHandler.END


def predict_cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


def main() -> None:
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_))
    dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('add', add)],
                                               states={ADD: [MessageHandler(Filters.text & ~Filters.command, add_v2)]},
                                               fallbacks=[CommandHandler('a_cancel', add_cancel)]))
    dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('delete', delete)],
                                               states={DEL: [CallbackQueryHandler(delete_v2)]},
                                               fallbacks=[CommandHandler('d_cancel', delete_cancel)]))
    dispatcher.add_handler(CommandHandler('favorites', favorites))
    dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('set_notifications', set_notifications)],
                                               states={TIME: [MessageHandler(Filters.text & ~Filters.command, set_notifications_v2)]},
                                               fallbacks=[CommandHandler('s_cancel', set_notifications_cancel)]))
    dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler('predict', predict)],
                                               states={PRED: [CallbackQueryHandler(predict_v2)]},
                                               fallbacks=[CommandHandler('p_cancel', predict_cancel)]))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
