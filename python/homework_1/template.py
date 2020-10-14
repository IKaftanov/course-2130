"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    if number % 20 == 0:
        return number
    return number - (number % 20) + 20



def t2(string):
    b = []
    string = string.split()
    for i in string:
        i = i[::-1]
        b.append(i)
    s = ' '.join(b)
    return s


def t3(dictionary):
    strings = []
    for i in dictionary:
        strings.append('{}: {}'.format(i, dictionary[i]))
    return '; '.join(strings)


def t4(string, sub_string):
    inverse_string = string[::-1]
    return sub_string in inverse_string


def t5(strings):
    b = []
    p = []
    m = []
    result = []
    for i in range(len(strings)):
        strings[i] = strings[i].replace(' ', '')
        b.append(strings[i])
    for j in range(len(b)):
        if b[j].isdigit():
            p.append(b[j])
    for element in p:
        element = list(element)
        if int(element[0]) * int(element[1]) * int(element[2]) == int(element[3]):
            m.append(element)
    for r in m:
        r = ' '.join(r)
        result.append(r)
    return result


def t5(strings):
    b = []
    for string in strings:
        try:
            x, y, z, mult = [int(i) for i in string.split()]
            if f'{x} {y} {z} {x*y*z}' == string and (x >= 0 and y >= 0 and z >= 0):
                b.append(string)
        except ValueError:
            continue
    return b


def t6(string):
    while string.find('#') >= 0:
        i = string.find('#')
        string = string[:max(0, i - 1)] + string[i + 1:]
    return string


def t7(lst):
    b = []
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            b.append(lst[i])
    return sum(b)


def t8(string):
    num_list = []
    num = ''
    for i in string:
        if i.isdigit():
            num = num + i
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return(max(num_list))


def t9(number):
    return f'{number:05d}'


def t10(string):
    d = {"GG": "G", "BG": "R", "RG": "B", "BR": "G", "GB": "R", "GR": "B", "RB": "G", "RR": "R", "BB": "B"}
    while len(string) > 1:
        s = ""
        for i in range(len(string) - 1):
            s = s + d.get(string[i:i + 2])
        string = s
    return string


def t11(lst):
    b = []
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            b.append(i)
    if b:
        return min(b)
    else:
        return -1


import re
def t12(lst):
    b = []
    p = []
    for i in lst:
        result = re.findall(r'[0-9|\ |\-|\(|\)|\+]{10,17}[0-9|\ |\-|\(|\)]', i)
        for j in result:
            b.append(j)
    for number in b:
        number = number.replace('+', '').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if number.startswith('7'):
            number = number.replace('7', '8', 1)
        p.append(number)
    return p


def t13(number_1, number_2):
    b = list(str(number_1))
    p = list(str(number_2))
    m = []
    if len(b) > len(p):
        slice = b[:(len(b) - len(p))]
        for i in range(len(p)):
            number = int(b[(len(b) - len(p)) + i]) + int(p[i])
            slice.append(number)
    else:
        if len(p) > len(b):
            slice = p[:(len(p) - len(b))]
            for i in range(len(b)):
                number = int(p[(len(p) - len(b)) + i]) + int(b[i])
                slice.append(number)
        if len(b) == len(p):
            slice = []
            for i in range(len(b)):
                number = int(b[i]) + int(p[i])
                slice.append(number)
    for j in slice:
        result = int(j)
        m.append(result)
    return int(''.join(map(str, m)))


def t14(string):
    for list in string:
        list = string.split()
    b = []
    dict = {'+':   'Plus',
        '-':   'Minus',
        '*':   'Times',
        '/':   'Divided By',
        '**':  'To The Power Of',
        '=':   'Equals',
        '!=':  'Does Not Equal',
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
    for i in range(len(list)):
        if list[i] in dict:
            b.append(dict[list[i]])
    return ' '.join(b)


def t15(lst):
    b = []
    c = []
    for i in range(len(lst)):
        b.append(lst[i][i])
        c.append(lst[i][len(lst) - (i + 1)])
    return sum(b + c)

