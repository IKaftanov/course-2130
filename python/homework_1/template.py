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
    return (number + 19) // 20 * 20


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`

    Данный код писался дерепан модаз
    """
    return ' '.join(word[::-1] for word in string.split())


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return '; '.join([str(key) + ': ' + str(value) for key, value in dictionary.items()])


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока

    Забавно будет проверить на строке tenet и подстроке net и ten
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    strings_filtered = []
    for i in strings:
        x, y, z, a = list(map(int, i.split()))
        if x * y * z == a:
            strings_filtered.append(i)
        else:
            pass
    return strings_filtered


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    while True:
        result = re.sub(r'\w#', '', string)
        if result == string:
            break
        string = result
    if '#' in string:
        return ''
    else:
        return string


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    return sum([i for i in lst if lst.count(i) <= 1])


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    return max(list(map(int, re.findall('[0-9]+', string))))


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return "{0:0=5d}".format(number)


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
    mixes = {'BG': 'R', 'RG': 'B', 'BR': 'G', 'GB': 'R', 'GR': 'B', 'RB': 'G'}  # задаем результаты смешивания цветов
    if len(string) > 1:
        sub_string = []
        for i in range(len(string) - 1):
            x, y = string[i], string[i + 1]
            if x == y:
                sub_string.append(x)
            else:
                sub_string.append(mixes[x + y])
        return t10(''.join(sub_string))
    else:
        return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    eq_sum_ind = [i for i in range(len(lst)) if sum(lst[:i]) == sum(lst[i + 1:])]
    if len(eq_sum_ind) >= 1:
        return eq_sum_ind[0]
    else:
        return -1


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    numbers = []
    for i in lst:
        numbers.extend(
            re.findall(r'\+?\d[( -]?\d{3}?[) -]?\d{3}[ -]?\d{2}[ -]?\d{2}', i))
    numbers_form = [''.join(re.findall(r'\d', i.replace('+7', '8'))) for i in numbers]
    return numbers_form


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416

    Можно было бы обозвать функцию "Математика от Даяны Ривас"
    """
    x = "{0:0={dig}d}".format(number_1, dig=max(len(str(number_1)), len(str(number_2))))
    y = "{0:0={dig}d}".format(number_2, dig=max(len(str(number_1)), len(str(number_2))))
    return int(''.join(map(str, list((i + j for i, j in zip(map(int, x), map(int, y)))))))


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
    words = {'+': 'Plus',
             '-': 'Minus',
             '*': 'Times',
             '/': 'Divided By',
             '**': 'To The Power Of',
             '=': 'Equals',
             '!=': 'Does Not Equal', '0': 'Zero',
             '1': 'One', '2': 'Two',
             '3': 'Three', '4': 'Four',
             '5': 'Five', '6': 'Six',
             '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    return ' '.join(map(lambda dig: words[dig], string.split()))


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    return sum(lst[i][i] for i in range(len(lst))) + sum(lst[i][len(lst) - i - 1] for i in range(len(lst)))
