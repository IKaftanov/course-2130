"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций происходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""
import re


def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    return number - number % 20 + 20 if number % 20 else number


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`

    """
    result = []
    for word in list(string.split()):
        result.append(word[::-1])
    return (' '.join(result))


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return '; '.join(f'{key}: {value}' for key, value in dictionary.items())


def t4(string, sub_string):
    """
    Необходимо проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    answer = []
    for line in strings:
        line = line.split()
        if int(line[0]) * int(line[1]) * int(line[2]) == int(line[3]):
            answer.append(' '.join(line))
        else:
            pass
    return answer


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    answer = ''
    for letter in string:
        if letter == "#":
            answer = answer[:-1]
        else:
            answer += letter
    return answer


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    return sum([i for i in lst if lst.count(i) == 1])


def t8(string):
    """
    Найдите все последовательности чисел в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    return max(list(map(int, re.findall(r'\d+', string))))


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return f'{number:05d}'


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

    def colour_maker(c1, c2):
        if c1 == c2:
            return c1
        elif (c1 == 'G' and c2 == 'B') or (c2 == 'G' and c1 == 'B'):
            return 'R'
        elif (c1 == 'G' and c2 == 'R') or (c2 == 'G' and c1 == 'R'):
            return 'B'
        else:
            return 'G'

    new_string = ''
    if len(string) > 1:
        for i in range(len(string) - 1):
            new_string += colour_maker(string[i], string[i + 1])
        return t10(new_string)
    else:
        return string[0]


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что суммы элементов левой и правой частей списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    answer = []
    for i, value in enumerate(lst):
        if (sum(lst[:i]) == sum(lst[:i:-1])): # А если убрать сумму, то можно проверять и простое равенство левой и правой части
            answer.append(i)
    if answer == []:
        return -1
    else:
        return answer[0]


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    regex = r'(\+?\d(\s|-|\()?\d{3}(\s|-|\))?\d{3}((\s|-)?\d{2}){2})'
    telephones = []
    for element in lst:
        for i in re.findall(regex, element):
            if str(i[0]).startswith('+7'):
                telephones.append(''.join(i for i in i[0].replace('+7', '8') if i.isdigit()))
                # другой возможный способ, используя несколько раз replace
                # telephones.append(i[0].replace('+7', '8').replace('-', '').replace(' ', '').replace('(', '').replace(')', ''))
            else:
                # Для случая, если телефон начинается просто с 7 (не +7)
                tel = '8' + str(i[0])[1:]
                telephones.append(''.join(i for i in tel if i.isdigit()))
    return telephones


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    answer = []
    while number_1 != 0 or number_2 != 0:
        answer.insert(0, number_1 % 10 + number_2 % 10)
        number_1, number_2 = (number_1 // 10), (number_2 // 10)
    if number_1 == 0 or number_2 == 0:
        answer.insert(0, number_1 + number_2)
    return int(''.join(map(str, answer)))


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выражение

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
    mapping = {'+': 'Plus',
               '-': 'Minus',
               '*': 'Times',
               '/': 'Divided By',
               '**': 'To The Power Of',
               '=': 'Equals',
               '!=': 'Does Not Equal',
               '0': 'Zero',
               '1': 'One',
               '2': 'Two',
               '3': 'Three',
               '4': 'Four',
               '5': 'Five',
               '6': 'Six',
               '7': 'Seven',
               '8': 'Eight',
               '9': 'Nine',
               '10': 'Ten'}
    new_line = ''
    for element in string.split():
        if element in mapping.keys():
            new_line += mapping.get(element) + ' '
    return new_line[:-1]


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    result = 0
    for i, line in enumerate(lst):
        result += line[i]
        result += line[len(line) - i - 1]
    return result

