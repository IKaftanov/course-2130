# Мелешкин Артём э541
# Проект: консольная графика (погода)

# Выгружаем нужные модули

import time
import os
import random
from pyowm import OWM

# Вводим необходимые данные: название города и код страны на латинице (две буквы), App ID на openweathermap.org
# My App ID - 783f15536504b770adafb7c5937b0b7b

city = input('Введите название города: ')
country = input('Введите код страны: ')
place = city + ',' + country
appid = input('Введите ваш App ID на сайте openweathermap.org: ')

# Парсим данные с сайта

owm = OWM(appid)
mgr = owm.weather_manager()

observation = mgr.weather_at_place(place)
w = observation.weather

t = w.status

# Задаём дополнительную функцию, чтобы задать направление ветра


def wind1(a):
    grads = [45, 90, 135, 180, 225, 270, 315, 360]
    dirs = ["северо-восточный", "восточный", "юго-восточный",
            "южный", "юго-западный", "западный", "северо-западный"]
    for i in range(len(grads) - 1):
        if grads[i] - 22.5 <= a <= grads[i + 1] - 22.5:
            return dirs[i]
    return 'северный'


# Задаём функцию и строки для анимации погоды
# Чтобы анимация корректно работала в PyCharm, необходимо включить флажок "Emulate terminal in output console"
# в меню "Edit Run Configuration"

def anim(t_):
    stri = ''
    if t_ == 'Snow':
        k = ' * '
    elif t_ == 'Rain':
        if 135 > w.wind()['deg'] > 45:
            k = ' / '
        elif 315 > w.wind()['deg'] > 225:
            k = ' \\ '
        else:
            k = ' | '
    elif t_ == 'Mist':
        k = '~_-'
    else:
        k = '   '
    for i in range(25):
        if t_ == 'Mist':
            a = random.randrange(0, 3)
        else:
            a = random.randrange(0, 6)
        if a != 0:
            stri += '   '
        else:
            stri += k
    return stri


cl1 = '     00000000        000000000             00000     ' + 22 * ' '
cl2 = '  00000000000000  00000000000000      0000000000000  ' + 22 * ' '
cl3 = '00000000000000000000000000000000000000000000000000000' + 22 * ' '
cl4 = '00000000000000000000000000000000000000000000000000000' + 22 * ' '
cl5 = '  000000000000000000000000000000000000000000000000   ' + 22 * ' '
cl6 = '        000000000000000000000000000000000000         ' + 22 * ' '

sun1 = '   ********   ' + ' ' * 61
sun2 = ' ************ ' + ' ' * 61
sun3 = '**************' + ' ' * 61

th = 0


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


ian = 0

# Вывод анимации

while True:
    cls()
    print('Прогноз погоды в городе', city, '|', country, '|', 'Status:', w.detailed_status.upper())
    print('-------------------------------------------------------------------------------------------------------')
    print('Температура воздуха:', w.temperature('celsius')['temp'], 'градусов Цельсия')
    print('Ветер', wind1(w.wind()['deg']), 'со скоростью', w.wind()['speed'], 'метров в секунду')
    print('Влажность воздуха:', w.humidity, 'процентов')
    if w.status == 'Clear':
        print(sun1[ian:] + sun1[:ian], sep='', end='\n')
        print(sun2[ian:] + sun2[:ian], sep='', end='\n')
        print(sun3[ian:] + sun3[:ian], sep='', end='\n')
        print(sun3[ian:] + sun3[:ian], sep='', end='\n')
        print(sun2[ian:] + sun2[:ian], sep='', end='\n')
        print(sun1[ian:] + sun1[:ian], sep='', end='\n')
    if w.status == 'Clouds' or (w.status == 'Thunderstorm' and str(th)[-1] != '0' and str(th)[-1] != '2'):
        print(cl1[ian:] + cl1[:ian], sep='', end='\n')
        print(cl2[ian:] + cl2[:ian], sep='', end='\n')
        print(cl3[ian:] + cl3[:ian], sep='', end='\n')
        print(cl4[ian:] + cl4[:ian], sep='', end='\n')
        print(cl5[ian:] + cl5[:ian], sep='', end='\n')
        print(cl6[ian:] + cl6[:ian], sep='', end='\n')
    if w.status == 'Thunderstorm' and (str(th)[-1] == '0' or str(th)[-1] == '2'):
        print('Z' * 75, sep='', end='\n')
        print('Z' * 75, sep='', end='\n')
        print('Z' * 75, sep='', end='\n')
        print('Z' * 75, sep='', end='\n')
        print('Z' * 75, sep='', end='\n')
        print('Z' * 75, sep='', end='\n')
    else:
        print(anim(t)[ian:] + anim(t)[:ian], sep='', end='\n')
        print(anim(t)[ian + 1:] + anim(t)[:ian + 1], sep='', end='\n')
        print(anim(t)[ian + 2:] + anim(t)[:ian + 2], sep='', end='\n')
        print(anim(t)[ian + 3:] + anim(t)[:ian + 3], sep='', end='\n')
        print(anim(t)[ian + 4:] + anim(t)[:ian + 4], sep='', end='\n')
        print(anim(t)[ian + 5:] + anim(t)[:ian + 5], sep='', end='\n')
    if w.status == 'Mist':
        time.sleep(0.7)
    if w.status == 'Thunderstorm':
        time.sleep(0.2)
    else:
        time.sleep(0.3)
    ian += 1
    th += 1
    if ian is len(anim(t)):
        ian = 0
