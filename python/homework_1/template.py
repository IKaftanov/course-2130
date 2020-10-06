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
    return number if not number % 20 else (number + 20) - (number + 20) % 20


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    return ' '.join([word[::-1] for word in string.split()])


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    items = list(dictionary.items())
    string = ''
    for item in items:
         string += str(item[0])+': '+str(item[1])+'; '
    return string[:-2]


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    filtered_strings = []
    for string in strings:
        try:
            x, y, z, prod = [int(i) for i in string.split()]
            if f'{x} {y} {z} {x*y*z}' == string and x >= 0 and y >= 0 and z >= 0:
                filtered_strings.append(string)
        except ValueError:
            continue
    return filtered_strings


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    while string.find('#') != -1:
        index = string.find('#')
        string = string[:max(0, index-1)]+string[index+1:]
    return string


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    return sum([i for i in lst if lst.count(i) == 1])


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    return max([int(k) for k in ''.join([i if i.isnumeric() else ' ' for i in string]).split()])


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return ('00000'+str(number))[-5:] if len(str(number)) < 5 else str(number)


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
    def new_col(col1, col2):
        if col1 == col2:
            new = col1
        elif col1+col2 == 'BG' or col2+col1 == 'BG':
            new = 'R'
        elif col1+col2 == 'RG' or col2+col1 == 'RG':
            new = 'B'
        else:
            new = 'G'
        return new
    
    if len(string) != 1:
        new_cols = ''
        for i in range(len(string)-1):
            new_cols += new_col(string[i], string[i+1])
        return t10(new_cols)
        
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
    for i, k in enumerate(lst):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i
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
    import re
    REG_EXPR = r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}'
    comp_reg_expr = re.compile(REG_EXPR)
    numbers = []
    for string in lst:
        number = comp_reg_expr.findall(string)[0]
        number = number.translate({ord(i): None for i in [' ', '+', '-', '(', ')']})
        number = '8'+number[1:]
        numbers.append(number)
    return numbers


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    out = ''
    wid = max(len(str(number_1)), len(str(number_2)))
    number_1 = '0'*(wid-len(str(number_1)))+str(number_1)
    number_2 = '0'*(wid-len(str(number_2)))+str(number_2)
    for i, k in zip(number_1, number_2):
        out += str(int(i) + int(k))
    return int(out)


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
    mapping = { '+': 'Plus ',
              '-':   'Minus ',
              '*':   'Times ',
              '/':   'Divided By ',
              '**':  'To The Power Of ',
              '=':   'Equals ',
              '!=':  'Does Not Equal ', 
              '1':   'One ', 
               '2':  'Two ', 
               '3':  'Three ', 
               '4':  'Four ', 
               '5':  'Five ', 
               '6':  'Six ', 
               '7':  'Seven ', 
               '8':  'Eight ', 
               '9':  'Nine ', 
               '10': 'Ten '}
    for i in set(string.split()):
        string = string.replace(i, mapping[i])
    return ' '.join(string.split())


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    out = 0
    i = 0
    for string in lst:
        out += string[i] + string[-i-1]
        i += 1
    return out