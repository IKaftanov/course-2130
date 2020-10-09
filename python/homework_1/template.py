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
    return (number - number % 20) + 20



def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    list0 = string.split()
    list1 = ''
    for i in list0:
        list1 += i[::-1] + ' '
    list1 = list1.strip()
    return list1

t2('dsf ecs ewd')
def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    list0 =''
    for key, value in dictionary.items():
        point = key + ": " + str(value) + ';'
        list0 += point
    return list0


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
    list0 = ''
    for i in string:
        if i == '#':
            list0 = list0[:-1]
        else:
            list0 += i
    return list0



def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    return sum([i for i in lst if lst.count(i) == 1])

def t8(string):
    import re
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    return max(map(int, re.findall('[0-9]+', string)))


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return f'{number:05d}'


def t10(string):
  
    
    
    while len(string) > 1:
        col = ['R','G','B']
        string0 = []
        for i in range(len(string)-1):
            col1, col2 = string[i], string[i+1]
            if col1 == col2:
                string0.append(col1)
            else:
                col.remove(col1)
                col.remove(col2)
                string0.append(col)
        return string0
    return string0
                
t10('RG')        
    
col = ['R','G','B']
col.remove('R')
return col
    while len(string) > 1:
        if len(string) != 2:
            list0 = {}


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    for i in range(1, len(lst)-1):
        if sum([int(x) for x in lst[:i]]) == sum([int(x) for x in lst[i+1:]]):
            return i
    return -1 
       


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
    pass


def t14(string):
    
    operator = {
        '+':   'Plus ',
        '-':   'Minus ',
        '*':   'Times ',
        '/':   'Divided By ',
        '**':  'To The Power Of ',
        '=':   'Equals ',
        '!=':  'Does Not Equal '
    }
    number = [
        'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
    ]

    left, op, right = string.split()

    return f'{number[int(left)]} {operator[op]}{number[int(right)]}'


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
   return sum(lst[i][i] for i in range(len(lst))) + sum(lst[i][len(lst) - i - 1] for i in range(len(lst)))

