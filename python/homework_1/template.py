"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


import re

def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    a = 0
    if number % 20 == 0:
        a += number
    else:
        a += number + 20 - (number % 20)
    return a

def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    ten = string.split(' ')
    tenet = list()
    for n in range(len(ten)):
        tenet.append(ten[n][::-1])
    a = ' '
    return a.join(tenet)


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    ls = ['{}: {}'.format(key, value) for key, value in dictionary.items()]
    string = '; '.join(ls)
    return string


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return bool(string.find(sub_string[::-1]) + 1)


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    filtered_str = []
    for i in range(len(strings)):
        my_string = ''
        new_lst = []
        new_lst += str(strings[i]).split(' ')
        if len(new_lst) == 4:
            x = new_lst[0]
            y = new_lst[1]
            z = new_lst[2]
            xyz = new_lst[3]
            if x.isdigit() and y.isdigit() and z.isdigit() and xyz.isdigit():
                x = int(x)
                y = int(y)
                z = int(z)
                xyz = int(xyz)
            my_string = ' '.join(new_lst)
            if x * y * z == xyz:
                filtered_str.append(my_string)
    return filtered_str


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    st = ''

    for i in string:
        if i == '#' and len(st) > 0:
            st = st[:-1]
        else:
            st += i
    return st.replace('#', '')

def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    a = 0
    for i in set(lst):
        if lst.count(i) == 1:
            a += i

    return a

def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    a = ''
    for i in string:
        if i.isdigit():
            a += i
        else:
            a += " "
    a = set(a.split(' '))
    a.remove('')
    max_el = -1
    for j in a:
        max_el = max(max_el, int(j))
    return max_el


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    number_str = str(number)
    num_list = [number_str]
    five_digit = number_str.rjust(5, "0")
    return five_digit


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """
    string = string.replace(' ', '')
    a = ''

    while len(string) > 1:
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                a += string[i]
            elif string[i] == 'R':
                if string[i + 1] == 'G':
                    a += 'B'
                else:
                    a += 'G'
            elif string[i] == 'G':
                if string[i + 1] == 'R':
                    a += 'B'
                else:
                    a += 'R'
            elif string[i] == 'B':
                if string[i + 1] == 'R':
                    a += 'G'
                else:
                    a += 'R'
        string = a
        a = ''

    return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    sm1 = 0
    sm2 = 0
    result = -1
    for i in range(len(lst)):
        sm1 = sum(lst[i + 1:])
        sm2 = sum(lst[:i])
        if sm1 == sm2:
            result = i
            break
    return result


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    result = []
    for i in range(len(lst)):
        res = re.findall(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}', lst[i])
        for j in range(len(res)):
            phone = re.sub(r'\s*([()+*/-])\s*', '', res[j]).replace(' ', '')
            if phone.startswith('7'):
                phone = '8' + phone[1:]
            result.append(phone)
    return result


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    good_list = []
    while number_1 or number_2:
        number_1, mod_1 = divmod(number_1, 10)
        number_2, mod_2 = divmod(number_2, 10)
        good_list = [str(mod_1 + mod_2)] + good_list
    number = ''.join(good_list)
    if number == '':
        number = 0
    return int(number)


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """

    def num2word(num):
        words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                 90: 'Ninety', 0: 'Zero'}

        div, mod = divmod(num, 10)

        if div and mod:
            return '{} {}'.format(words[div * 10], words[mod])
        elif mod == 0:
            return words[div * 10]
        else:
            return words[mod]

    symbols = {'+': 'Plus',
               '-': 'Minus',
               '*': 'Times',
               '/': 'Divided By',
               '**': 'To The Power Of',
               '=': 'Equals',
               '!=': 'Does Not Equal',
               }
    res = []
    for char in string.split(' '):
        if char.isdigit():
            res.append(num2word(int(char)))
        elif char in symbols.keys():
            res.append(symbols[char])
        else:
            res.append(char)

    return ' '.join(res)

def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    a = 0
    for i in range(len(lst)):
        a += lst[i][i]
        j = len(lst) - 1 - i
        a += lst[i][j]
    return a
