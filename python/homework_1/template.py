def t1(number):
    return int(round(number / 20) * 20)
t1(21)
t1(-5)

def t2(string):
    inverted_string = []
    for i in list(string.split()):
        inverted_string.append(i[::-1])
    return ' '.join(inverted_string)
string = 'abc abc abc'
t2(string)

def t3(dictionary):
    return '; '.join(f'{key}: {value}' for key, value in dictionary.items())
dictionary = {'Фрукты': ['яблоко', 'груша', 'апельсин'], 'Овощи': ['помидоры', 'огурцы', 'перец']}
t3(dictionary)

def t4(string, sub_string):
    if string.find(sub_string[::-1]) == 0:
        return 'FALSE'
    else:
        return 'TRUE'
string = 'abcd'
sub_string = 'cb'
t4(string, sub_string)

def t5(strings):
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
            continue
    return result
strings = ['5 3 8 4', '3 2 1 6', '5 2 7 70', '0 2 2 0', '1 1 5 7', '2 8 9 0']
t5(strings)

def t6(string):
    string_str = "abc#d##с"
    string_res = ""
    for vars in string_str:
        if vars != "#":
            string_res += vars
        else:
            string_res = string_res[:-1]
    return string_res
t6(string)

def t7(lst):
    unique_objects = []
    return sum(set(x for x in lst if lst.count(x) == 1))
lst = [4, 5, 7, 5, 4, 8]
t7(lst)

import re
def t8(string):
    re.findall('(\d+)', 'gh12cdy695m1')
    string = re.findall('(\d+)', 'gh12cdy695m1')
    return max(string)
t8(string)

def t9(number):
    return '{:05}'.format(number)
t9(5)

def t10(string):
    color_combinations = {'GG': 'G', 'BB': 'B', 'RR': 'R', 'BG': 'R', 'GB': 'R',
                          'RG': 'B', 'GR': 'B', 'BR': 'G', 'RB': 'G'}
    if len(string) > 1:
        string = ''.join([color_combinations[string[i] + string[i + 1]]
                          for i in range(len(string) - 1)])
        return t10(string)
    else:
        return string
string = 'RRGBRGBB'
t10(string)

def t11(lst):
    for i in range(1, len(lst) - 1):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return i
    return -1
lst = [1, 2, 3, 5, 3, 2, 1]
t11(lst)

import re
def t12(lst):
    tel_num = []
    for telephone_number in lst:
        t = re.compile(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}').findall(telephone_number)[0]
        t = t.replace(' ', '')
        t = t.replace("-", "")
        t = t.replace("+", "")
        t = t.replace(")", "")
        t = t.replace("(", "")
        t = '8' + t[1:]
        tel_num.append(t)
        return tel_num
lst = ['Что-то происходит бла бла бла +7495 123-45-67']
t12(lst)

def t13(number_1, number_2):
    number_3 = [int(x) + int(y) for x, y in zip(number_1, number_2)]
    return ''.join((str(x) for x in number_3))
number_1 = [2, 4, 8]
number_2 = [2, 0, 8]
t13(number_1, number_2)

def t14(string):
    operators = {'+': ' Plus ', '-': ' Minus ', '*': ' Times ', '/': ' Divided By ',
                 '**': ' To The Power Of ', '=': ' Equals ', '!=': ' Does Not Equal '}
    numbers = {'0': 'zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
                   '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    operators.update(numbers)
    expression = string.split()
    for i in range(len(expression)):
        expression[i] = operators[expression[i]]
    return ''.join(expression).strip()
string = '4 ** 9'
t14(string)

def t15(lst):
    length = len(lst)
    r1 = 0
    r2 = 0
    for i in range(length):
        r1 += lst[i][length - i - 1]
        r2 += lst[i][i]
    return r1 + r2
lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
t15(lst)
