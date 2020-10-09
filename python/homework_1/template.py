
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
    m = (number//20)*20 + 20
    if number//20 == number/20:
        return number
    else:
        return m


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    return ' '.join(word[::-1] for word in string.split(" "))


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    sd = str(dictionary)
    return sd.replace('{', '').replace('}', '').replace(',', ';').replace("'", "")
    pass

def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    rs = string[::-1]
    if sub_string in rs:
        return True
    else:
        return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    strings_filtered = []
    for item in strings:
        if int(item[-1]) == int(item[0]) * int(item[2]) * int(item[4]):
            strings_filtered.append(item)
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
    string_proc = ''
    for elem in string:
        if elem != '#':
            string_proc += elem
        else: 
            string_proc = string_proc[:-1]
    return string_proc
    pass


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    lst_uniq_sum = 0 
    for item in lst:
        if lst.count(item) == 1:
            lst_uniq_sum += item
    return lst_uniq_sum



def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    import re
    reg = re.findall(r'\d+', string)
    m = max(list(map(int, reg)))
    return m


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    t = len(str(number))
    s = 5 - t
    if t < 5:
        return '0'*s + str(number)
    else:
        return str(number)



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
    def f1(string):
        m = ''
        colors = {'R', 'G', 'B'}
        for i in range(len(string)-1):
            x = {string[i], string[i+1]}
            if len(x) == 2:
                m += (colors - x).pop()
            else:
                m += x.pop()
        return m

    while len(string) > 1:
        string = f1(string)

    return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    s = -1
    for i in range(len(lst)):
        sum_left = sum([int(j) for j in lst[:i]])
        sum_right = sum([int(j) for j in lst[i+1:]])
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i
            s += i+1
    return s
    pass

def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    res = []
    str_list = str(lst)
    r = re.findall(r'(\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2})', str_list)
    for i in r:
        j = i.replace('+7', '8').replace(' ', '').replace(')', '').replace('(', '').replace('-', '')
        res.append(j)
    return res


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    n1 = str(number_1)
    n2 = str(number_2)
    n3 = ''
    if len(n1) < len(n2):
        n1 = '0'*(len(n2) - len(n1)) + n1
    else:
        n2 = '0'*(len(n1) - len(n2)) + n2
    for i in range(len(n1)):
        n3 += str(int(n1[i]) + int(n2[i]))
    return int(n3)


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
    ops = {'+':   'Plus ', '-':   'Minus ', '*':   'Times ', '/':   'Divided By ', '**':  'To The Power Of ', '=':   'Equals ', '!=':  'Does Not Equal '}
    nums = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    exp = string.split()
    return nums.get(exp[0]) + ' ' + ops.get(exp[1]) + nums.get(exp[2])


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    s = 0
    for i in range(len(lst)):
        j = len(lst) - 1 - i
        s += lst[i][i] + lst[i][j]
    return s    
