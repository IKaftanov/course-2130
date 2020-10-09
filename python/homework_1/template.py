import re
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
    for i in range(20):
        if number % 20 == 0:
            return number
        else:
            number = number + 1
        pass
    pass


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    split = string.split()
    reverse = []

    for i in split:
        reverse.append(str(i[::-1]))

    return ' '.join(reverse)
    pass


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    items = dictionary.items()
    aux = []
    for i in items:
        aux.append(str(i[0]) + ': ' + str(i[1]))
    return '; '.join(aux)
    pass


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if sub_string[::-1] in string:
        return True
    else:
        return False
    pass


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    regex = re.compile(r'^\[1-9]+\s\[1-9]+\s\[1-9]+\s\[1-9]+\*\[1-9]+\*\[1-9]+$')
    filtered = [*filter(regex.match, strings)]

    return filtered
    pass


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    newstring = ''
    for i in range(len(string)):
        if string[i] != '#':
            newstring = newstring + string[i]
        else:
            newstring = newstring[:-1]
    return newstring
    pass


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    unique_vals = []

    for i in set(lst):
        if lst.count(i) == 1:
            unique_vals.append(i)
        else:
            pass

    return sum(unique_vals)
    pass


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    num = re.findall(r'\d+', string)
    num = map(int, num)
    return max(num)
    pass


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    lenght = len(str(abs(number)))
    zeros = (5 - lenght) * '0'
    return zeros + str(number)
    pass


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
    def colorsum(color1, color2):
        if color1 == color2:
            return color1
        elif color1 == 'G':
            if color2 == 'B':
                return 'R'
            else:
                return 'B'
        elif color1 == 'B':
            if color2 == 'G':
                return 'R'
            else:
                return 'G'
        else:
            if color2 == 'G':
                return 'B'
            else:
                return 'G'
        pass
    split = string

    sumcols = ''
    while len(split) > 1:
        for i in range(len(split)-1):
            sumcols = sumcols + colorsum(split[i], split[i+1])
        split = sumcols
        sumcols = ''
    return ' '.join(split)
    pass


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    index = -1
    for i in range(len(lst)):
        if sum(lst[0:i]) == sum(lst[i+1:]):
            index = index + 1 + i
            break
        else:
            pass
    return index
    pass


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """

    pass


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    len_1 = len(str(number_1))
    len_2 = len(str(number_2))
    summed = []

    if len_1 == len_2:
        for i in range(len_1):
            summed.append(str(int(str(number_1)[i]) + int(str(number_2)[i])))
        return int(''.join(summed))
    elif len_1 > len_2:
        diff = len_1 - len_2
        number_2 = number_2 * 10**diff
        for i in range(len_1):
            summed.append(str(int(str(number_1)[i]) + int(str(number_2)[i])))
        return int(''.join(summed))
    else:
        diff = len_2 - len_1
        number_1 = number_1 * 10**diff
        for i in range(len_2):
            summed.append(str(int(str(number_1)[i]) + int(str(number_2)[i])))
        return int(''.join(summed))
    pass


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
    math_dict = {'+':   ' Plus ',
                 '-':   ' Minus ',
                 '*':   ' Times ',
                 '/':   ' Divided By ',
                 '**':  ' To The Power Of ',
                 '=':   ' Equals ',
                 '!=':  ' Does Not Equal ',
                 '1': 'One', '2': 'Two',
                 '3': 'Three',
                 '4': 'Four',
                 '5': 'Five',
                 '6': 'Six',
                 '7': 'Seven',
                 '8': 'Eight',
                 '9': 'Nine',
                 '10': 'Ten'}

    newstring = ''
    string = string.split()
    for i in range(len(string)):
        newstring = newstring + math_dict[string[i]]
    return newstring
    pass


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    size = len(lst[0])
    if size == 1:
        return lst[0][0]*2

    diag_sum = 0

    for i in range(size):
        diag_sum += lst[i][i]

        diag_sum += lst[i][size-i-1]
    return diag_sum
    pass
