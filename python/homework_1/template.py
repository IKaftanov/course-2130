"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    def f(x):
        return int(round(x / 20) * 20)
    print(int(round(21 / 20) * 20))
    print(int(round(-5 / 20) * 20))
    
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    pass


def t2(string):
    def reverse_string(s):
        return s[::-1]
    print(reverse_string('abc abc abc'))
    
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    pass


def t3(dictionary):
    d = {'Фрукты': ['яблоко', 'груша', 'апельсин'], 'Овощи': ['помидоры', 'огурцы', 'перец']}
    for key, value in d.items():
        print(key, ':', ', '.join(str(num) for num in value), sep='')
        
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    pass


def t4(string, sub_string):
        def reverse_string(s):
        return s[::-1]
    print(reverse_string('cb'))

    def check(string, sub_string):
        if string.find(sub_string) == 0:
            print('NO')
        else:
            print('YES')
    string = 'abcd'
    sub_string = reverse_string('cb')
    check(string, sub_string)
    
    """
    проверить есть ли в строке инвертированная подстрока
    """
    pass


def t5(strings):
    strings = ['5 3 8 4', '3 2 1 6', '5 2 7 70', '0 2 2 0', '1 1 5 7', '2 8 9 0']
    result = []
    for data in strings:
        data = data.split()
        x = int(data[0])
        y = int(data[1])
        z = int(data[2])
        xyz = int(data[3])
        if int(x * y * z == xyz):
            result.append(' '.join(data))
        else:
            pass
    print(result)
    
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass


def t6(string):
    string_str = "abc#d##с"
    string_res = ""
    for vars in string_str:
        if vars != '#':
            string_res += vars
        else:
            string_res = string_res[:-1]
    print(string_res)

    string_str = "abc##d######"
    string_res = ""
    for vars in string_str:
        if vars != '#':
            string_res += vars
        else:
            string_res = string_res[:-1]
    print(string_res)

    string_str = "#######"
    string_res = ""
    for vars in string_str:
        if vars != '#':
            string_res += vars
        else:
            string_res = string_res[:-1]
    print(string_res)

    string_str = ""
    string_res = ""
    for vars in string_str:
        if vars != '#':
            string_res += vars
        else:
            string_res = string_res[:-1]
    print(string_res)
    
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    pass


def t7(lst):
    objects = [4, 5, 7, 5, 4, 8]
    unique_objects = []
    set(x for x in objects if objects.count(x) == 1)
    sum(set(x for x in objects if objects.count(x) == 1))
    
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    pass


def t8(string):
    import re
    re.findall('(\d+)', 'gh12cdy695m1')
    list = re.findall('(\d+)', 'gh12cdy695m1')
    print(list)
    maximum = max(list)
    print(maximum)
    
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    pass


def t9(number):
    '{:05}'.format(5)
    print('{:05}'.format(5))
    
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    pass


def t10(string):
        def triangle(row):
        color_combinations = {'GG': 'G', 'BB': 'B', 'RR': 'R', 'BG': 'R', 'GB': 'R', 'RG': 'B', 'GR': 'B', 'BR': 'G',
                              'RB': 'G'}
        if len(row) > 1:
            row = ''.join([color_combinations[row[i] + row[i + 1]]
                           for i in range(len(row) - 1)])
            return triangle(row)
        else:
            return row
    print(triangle(input().upper()))
    
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
    pass


def t11(lst):
        def find_index(lst, n):
        lst = [1, 2, 3, 5, 3, 2, 1]
        n = len(lst)
        for i in range(len(lst)):
            if sum(lst[0:i]) == sum(lst[i + 1:len(lst)]):
                return i
        return -1

    print(find_index(lst, n))

    def find_index(lst, n):
        lst = [1, 12, 3, 3, 6, 3, 1]
        n = len(lst)
        for i in range(len(lst)):
            if sum(lst[0:i]) == sum(lst[i + 1:len(lst)]):
                return i
        return -1

    print(find_index(lst, n))

    def find_index(lst, n):
        lst = [10, 20, 30, 40]
        n = len(lst)
        for i in range(len(lst)):
            if sum(lst[0:i]) == sum(lst[i + 1:len(lst)]):
                return i
        return -1

    print(find_index(lst, n))
    
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    pass


def t12(lst):
    import re
    text = ['Что-то происходит бла бла бла +7495 123-45-67']
    tel_num = []
    for telephone_number in text:
        t = re.compile(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}').findall(telephone_number)[0]
        t = t.replace(' ', '')
        t = t.replace("-", "")
        t = t.replace("+", "")
        t = t.replace(")", "")
        t = t.replace("(", "")
        t = '8' + t[1:]
        tel_num.append(t)
    print(tel_num)
    
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    pass


def t13(number_1, number_2):
    a = [2, 4, 8]
    b = [2, 0, 8]
    c = [x + y for x, y in zip(a, b)]
    print(''.join((str(x) for x in c)))
    
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    pass


def t14(string):
        def expr(x):
        operators = {'+': ' Plus ', '-': ' Minus ', '*': ' Times ', '/': ' Divided By ',
                     '**': ' To The Power Of ', '=': ' Equals ', '!=': ' Does Not Equal '}
        numbers = {'0': 'zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
                   '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
        operators.update(numbers)
        expression = x.split()
        for i in range(len(expression)):
            expression[i] = operators[expression[i]]
        return ''.join(expression).strip()

    print(expr('4 ** 9'))
    print(expr('10 - 5'))
    print(expr('2 = 2'))
    
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
    pass


def t15(lst):
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    length = len(arr)
    r1 = 0
    r2 = 0
    for i in range(length):
        r1 += arr[i][length - i - 1]
        r2 += arr[i][i]
    print(r1 + r2)
    
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    pass

