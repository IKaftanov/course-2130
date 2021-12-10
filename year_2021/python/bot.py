
import telebot
from telebot import types
#2055198971:AAE-cVyGydzLaraCPIY7pd8rUp3zrPerwI8

bot = telebot.TeleBot("2055198971:AAE-cVyGydzLaraCPIY7pd8rUp3zrPerwI8")
@bot.message_handler(commands=['start', 'help'])

def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('🍴Рестораны')
    item2 = types.KeyboardButton('💇‍♀️💇Салоны красоты')
    item3 = types.KeyboardButton('🌿Парки')
    item4 = types.KeyboardButton('🏛Выставки и музеи')
    item5 = types.KeyboardButton('🛍Продовольственные магазины')
    item6 = types.KeyboardButton('🍻🥂Бары')

    markup.add(item1,item2, item3,item4,item5,item6)

    bot.send_message(message.chat.id, 'Здравствйте, {0.first_name}, рады вас приветстсовать в чате с ботом района Хамовники. Выберите раздел, который вас интересует.'.format(message.from_user), reply_markup= markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🍴Рестораны':
            bot.send_message(message.chat.id, "1)Lure Oysterba (3-я улица Ямского Поля 9 с1) \r\n2)1.15 Kitchen+Bar (Пожарский переулок 15) \r\n3)Чемодан (Гоголевский бульвар 25) \r\n4)Winil Wine Bar (Зубовская 5/36) \r\n5)Аченти (Кропотненский переулок  \r\n6)Brisket BBQ (Смоленский б-р  15)"
                                              " \r\n7)Пинцерия Бонтемпи (Зубовская 5/36) \r\n8)Эларджи (Гагаринский переулок, д. 15а) \r\n9)Баба Марта (Гоголевский бульвар, д. 8 стр. 2) \r\n10)Журфак (Большой Афанасьевский переулок, д. 3) \r\n11)Винный базар (Комсомольский проспект, 14/1-2)"
                                              "\r\n12)Ресторан Воронеж (ул. Пречистенка 4) \r\n13)Ресторан La Scarpetta (Оболенский переулок, 9) \r\n14)IL Pizzaiolo (ул. Волхонка, д. 6) \r\n15)MOS Gastronomic Smart & Casual (ул. Трубецкая, 10) ")
        elif message.text == '💇‍♀️💇Салоны красоты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('💵Эконом')
            item2 = types.KeyboardButton('💵💵💵Премиум')
            back = types.KeyboardButton('↩️Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'💇‍♀️💇Салоны красоты'.format(message.from_user), reply_markup= markup)
        elif message.text == '🌿Парки':
            bot.send_message(message.chat.id, "1)Усадьба Трубецких в Хамовниках (Усачева, 1а) \r\n2)Парк «Новодевичьи пруды» (Новодевичья набережная) \r\n3)Сквер Девичьего поля (пр-д Девичьего Поля) \r\n4)Центральный парк культуры и отдыха им. М.Горькогo (ул. Крымский Вал, 9) \r\n5)Нескучный Сад (Пушкинская набережная) ")
        elif message.text == '🏛Выставки и музеи':
            bot.send_message(message.chat.id, "1)Музей-усадьба Л.Н. Толстого в Хамовниках (ул. Льва Толстого, д. 21) \r\n2) Галерея Классической Фотографии (Саввинская наб., 23, к.1) \r\n3)Музей Ар Деко (Лужнецкая наб., 2/4) \r\n4)Галерея искусств З.К. Церетели (ул. Пречистенка, д. 1)  \r\n5)Дом Бурганова Московский Государственный Музей (Большой Афанасьевский пер., 15, стр. 9)")
        elif message.text == '🛍Продовольственные магазины':
            bot.send_message(message.chat.id, "1)Магнолия (Комсомольский проспект, д. 25 корпус )  \r\n2)Дикси (Фрунзенская Набережная, 40) \r\n3)Кулинарная лавка братьев Караваевых (10 лет Октября, 9)  \r\n4)Седьмой Континен (Комсомольский проспект, 11) \r\n5)BILLA (Усачёва, 35 с1) n6) ГРАНД ГРОС(Комсомольский проспект, 48) \r\n7)Минута-маркет (Фрунзе Тимура, 11 к2) \r\n8)Продуктовый магазин №3 (Проспект девичьего поля 2) \r\n9)БЕЛОБОГ (Комсомольский проспект, 45) \r\n10)ГЕРМЕД (Плющиха, 42)")
        elif message.text == '🍻🥂Бары':
            bot.send_message(message.chat.id,"1)Винотека Виновники (пр-кт Комсомольский, д 28) \r\n2)Ви Ай Пи бар (Саввинская набережная, 21) \r\n3)Leto Lounge (Фрунзенская наб., 30, стр. 5) \r\n4)Smoke77 (Фрунзенская наб., 30/5) \r\n5)Dictatura Estetic (Гоголевский бульвар, 17) \r\n6)Сабфилд Бар (Фрунзенская наб., 46)  \r\n7)Choice Moscow (Лужнецкая наб., 2/4)  \r\n8)BAR LUCH (Большая Пироговская ул., 27стр) \r\n9)Розис Бар (ул. Тимура Фрунзе, 22) \r\n10)Greenside Bar (улица Ефремова, 10с1к4/)")
        elif message.text == '💵Эконом':
            bot.send_message(message.chat.id,"1)Espace De Beaute’ (улица Хамовнический Вал, 16)  \r\n2)Студия маникюра Luck ( Комсомольский проспект, 14/1к2) \r\n3)Академия красоты Selena (Пречистенка, 4 ст2) \r\n4)Салон красоты Lime ( Комсомольский проспект, 23/7) \r\n5)Центр красоты Долорес ( Большой Афанасьевский переулок, 12 ст2) \r\n6)Студия красоты ORO ( Языковский переулок, 5к6) "
                                             "\r\n7)Институт красоты Сенсави (Комсомольский проспект, 32к2) \r\n8)Парикмахерская Filini (улица Ефремова, 20)  \r\n9)Студия красоты LUCKY YOU (Комсомольский проспект, 3)  \r\n10)Салон красоты Острова ( Комсомольский проспект, 5/2) ")
        elif message.text == '💵💵💵Премиум':
            bot.send_message(message.chat.id, "1)Салон Мишель Экзертье (1-й Неопалимовский переулок, 14/1) \r\n2)Салон красоты Saco (Бурденко, 3) \r\n3)Центр здоровья и красоты Vобразе (Остоженка, 3/14) \r\n4)Спа-клуб Ревиталь (Коробейников переулок, 1) \r\n5)Салон красоты Nowe ( Комсомольский проспект, 41) \r\n6)Салон красоты jld Beauty ( Комсомольский проспект, 38/16) \r\n7)Салон красоты Dessange ( Коробейников переулок, 1) \r\n8)Салон красоты Моне (Комсомольский проспект, 19) \r\n9)Салон красоты Британа (улица Бурденко, 14) \r\n10)Студия красоты L-Studio ( Малая Пироговская улица, 8) ")
        elif message.text == '↩️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🍴Рестораны')
            item2 = types.KeyboardButton('💇‍♀️💇Салоны красоты')
            item3 = types.KeyboardButton('🌿Парки')
            item4 = types.KeyboardButton('🏛Выставки и музеи')
            item5 = types.KeyboardButton('🛍Продовольственные магазины')
            item6 = types.KeyboardButton('🍻🥂Бары')

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, '↩️Назад', reply_markup= markup)



bot.infinity_polling()