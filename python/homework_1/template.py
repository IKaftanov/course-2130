def t1(number):
    if number % 20 != 0:
        return number - number % 20 + 20  
    else:
        return number

def t2(string):
    inverted_string = []
    for i in list(string.split()):
        inverted_string.append(i[::-1])
    return ' '.join(inverted_string)

def t3(dictionary):
    return '; '.join(f'{key}: {value}' for key, value in dictionary.items())


def t4(string, sub_string):
    if string.find(sub_string[::-1]) == -1:
        return False
    else:
        return True

def t5(strings):
    result = []
    for data in strings:
        data = data.split()
        try:
            x = int(data[0])
            y = int(data[1])
            z = int(data[2])
            xyz = int(data[3])
            if x * y * z == int(xyz):
                result.append(' '.join(data))
        except ValueError:
            continue
    return result


def t6(string):
    string_res = ""
    for vars in string:
        if vars != "#":
            string_res += vars
        else:
            string_res = string_res[:-1]
    return string_res

def t7(lst):
    unique_objects = []
    return sum(set(x for x in lst if lst.count(x) == 1))

import re
def t8(string): 
    lst = re.findall(('\\d+'), string)
    return max(list(map(int, lst)))

def t9(number):
    return '{:05}'.format(number)

def t10(string):
    color_combinations = {'GG': 'G', 'BB': 'B', 'RR': 'R', 'BG': 'R', 'GB': 'R',
                          'RG': 'B', 'GR': 'B', 'BR': 'G', 'RB': 'G'}
    if len(string) > 1:
        string = ''.join([color_combinations[string[i] + string[i + 1]]
                          for i in range(len(string) - 1)])
        return t10(string)
    else:
        return string


def t11(lst):
    for i in range(1, len(lst) - 1):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return i
    return -1

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

def t13(number_1, number_2):
    number_3 = [int(x) + int(y) for x, y in zip(number_1, number_2)]
    return ''.join((str(x) for x in number_3))

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


def t15(lst):
    length = len(lst)
    r1 = 0
    r2 = 0
    for i in range(length):
        r1 += lst[i][length - i - 1]
        r2 += lst[i][i]
    return r1 + r2
