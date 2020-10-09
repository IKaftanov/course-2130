"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    x = int(number)
    if x % 20 == 0:
        return x
    else:
        return x // 20 * 20 + 20




def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """

    x = string.split()
    list = []
    r = ""
    for i in x:
        res = i[::-1]
        list.append(res)
        r = " ".join(list)
    return r



def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    r = ""
    list = []
    for key, value in dictionary.items():
        res = key + ": " + str(value)
        list.append(res)
        r = "; ".join(list)
    return r



def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    x = string
    y = sub_string
    reverse_y = y[::-1]
    if reverse_y in x:
        res = True
    else:
        res = False
    return res



def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    l = []
    try:
        for i in strings:
            x = i.split(" ")
            a = int(x[0])
            b = int(x[1])
            c = int(x[2])
            d = int(x[3])
            if d == a * b * c:
                l.append(i)
    except ValueError:
        pass
    return l


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    s1 = []

    for i in string:

        if i == '#':
            if s1:
                s1.pop()
        else:
            s1.append(i)
    return ''.join(s1)


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    try:
        list = []
        t = 0
        for k in lst:
            list.append(int(k))
            t += int(k)
        a = 0
        for i in range(len(list)):
            if list.count(list[i]) > 1:
                a += int(list[i])
            else:
                pass
        return t - a
    except ValueError:
        return 0



def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    x = string
    a = 0
    i = 0
    l = []
    while i < len(x):
        try:
            a = a * 10 + int(x[i])
        except ValueError:
            a = 0
        l.append(a)
        i += 1
    out = max(l)
    return out



def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """

    def l(num):
        a = 0
        while num != 0:
            a += 1
            num = num // 10
        return a

    if number <= 99999:
        t = 5 - l(number)
        out = "0" * t + str(number)
    else:
        out = str(number)
    return out



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

    def color(x):
        s = ["B", "G", "R"]
        i = 0
        result = ""
        while i < len(x) - 1:
            if x[i] == x[i + 1]:
                result = result + x[i]
            else:
                s.remove(x[i])
                s.remove(x[i + 1])
                result = result + s[0]
            i += 1
            s = ["B", "G", "R"]
        return result

    while len(string) > 1:
        string = color(string)
    return string

def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """

    def sum(list):
        t = 0
        for i in range(len(list)):
            t = t + int(list[i])
        return t

    a = 0
    for i in range(len(lst)):
        xl = lst[:i]
        xr = lst[i + 1:]
        if sum(xl) == sum(xr):
            return i
            a += 1
            break
        else:
            pass
    if a == 0:
        return -1




def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    list = []
    for str in lst:
        x = re.sub(r'\W', "", str)
        num = re.compile(r"(7\d{10}|8\d{10})")
        X = re.findall(num, x)
        X1 = X[0]
        X2 = "8" + X1[1:]
        list.append(X2)

    return list



def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    x1 = str(number_1)
    x2 = str(number_2)
    l = 0
    if len(x1) > len(x2):
        l = len(x1)
    else:
        l = len(x2)
    i = 1
    x = ""
    while i <= l:
        try:
            xi = int(x1[-i]) + int(x2[-i])
        except IndexError:
            try:
                xi = int(x1[-i])
            except IndexError:
                xi = int(x2[-i])
        xi = str(xi)
        x = xi + x
        i += 1
    return int(x)


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
    dict1 = {'**': 'To The Power Of', '10': 'Ten', '!=': 'Does Not Equal'}
    dict2 = {'+': 'Plus',
             '-': 'Minus',
             '*': 'Times',
             '/': 'Divided By',
             '=': 'Equals',
             '0': 'Zero', '1': 'One',
             '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
             '6': 'Six', '7': 'Seven',
             '8': 'Eight', '9': 'Nine'}
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    x = string
    for i in list1:
        x = x.replace(i, dict1[i])
    for i in list2:
        x = x.replace(i, dict2[i])
    return x

def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    b = 0
    for i in range(len(lst)):
        b = b + int(lst[i][i]) + int(lst[i][-i - 1])
    return b

