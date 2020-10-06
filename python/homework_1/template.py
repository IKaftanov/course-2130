"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста, не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""

import re

def t1(number):
    """
    Поправьте код что бы возвращаемое значение было следующим кратным 20

    Пример: number=21 тогда нужно вернуть 40

    """
    return (number + 19) // 20 * 20


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    
    налон йинег.
    """
    return ' '.join([word[::-1] for word in string.split()])


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return '; '.join([f'{key}: {value}' for (key, value) in dictionary.items()])


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированая подстрока
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    def func(string):
        x, y, z, p = list(map(int, string.split()))
        return string == f'{x} {y} {z} {x*y*z}'
    return list(filter(func, strings))


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
    return sum([x for x in lst if lst.count(x) == 1])


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    digits = re.findall(r'\d+', string)
    return max(list(map(int, digits)))

def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    if len(str(number)) <= 5:
        return '0' * (5 - len(str(number))) + str(number)
    else:
        return str(number)


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B R    R G   B R
    Результирующий цвет:   G       G      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод
    """       
    if len(string) > 1:
        intermediate_result = []
        s = [c for c in string if c in ('R', 'G', 'B')]
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if a == b:
                intermediate_result.append(a)
            else:
                intermediate_result.extend([i for i in ('R', 'G', 'B') if i != a and i != b])
        return t10(' '.join(intermediate_result))
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
    elements = [i for i in range(len(lst)) if sum(lst[:i]) == sum(lst[i + 1:])]
    if elements:
        return elements[0]
    else:
        return -1

def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +790112345678` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: ['Что-то происходит бла бла бла +790112345678 790112345678', 'Звони 790112345678 мне', 'По вопросам рекламы 890112345678']
    Выход: список номеров

    """
    result = []
    for string in lst:
        regexp = r'(\+?\d(\s|-|\()?\d{3}(\s|-|\))?\d{3}((\s|-)?\d{2}){2})'
        numbers = [''.join(re.findall(r'\d+', i[0].replace('+7', '8'))) for i in re.findall(regexp, string)]
        result.extend(numbers)
    return result

def t13(number_1, number_2):
    """
    Сложите два числа поэлементно:
        248
       +208
        4416
        не все поймут, но многие вспомнят
    """
    result = []
    while number_1 != 0 or number_2 != 0:
        result.append(number_1 % 10 + number_2 % 10)
        number_1 = number_1 // 10
        number_2 = number_2 // 10
        
    if result:
        return int(''.join(list(map(str, result[::-1]))))
    else:
        return 0


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
    mapping = { '+': 'Plus',
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
    return ' '.join(list(map(lambda x: mapping[str(x)], string.split())))


def t15(lst):
    """
    Найдите сумму элементов на диагонали 
    тогда уж диагоналЯХ -- главной и побочной

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    
    """
    return sum([l[i] + l[len(l)-i-1] for i, l in enumerate(lst)])
    