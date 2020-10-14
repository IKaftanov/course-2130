"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    i=0
    while (number+i)%20 !=0:
        i+=1
    return  number+i
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    pass


def t2(string):
    a = string[::-1]
    b = a.split()
    b.reverse()
    return ' '.join(b)
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    pass


def t3(dictionary):
    x = str(dictionary)
    y = x[1:-1]
    z = y.replace(',', ';')
    otvet = z.replace("'", '')
    return otvet
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    pass


def t4(string, sub_string):
    x = sub_string[::-1]
    return string.find(x) != -1
    """
    проверить есть ли в строке инвертированная подстрока
    """
    pass


def t5(strings):
    answer = []
    for i in strings:
        s = i.replace(' ', '')
        if s.isdigit() == True and int(i.split()[0]) * int(i.split()[1]) * int(i.split()[2]) == int(
                i.split()[3]) and len(i.split()) == 4:
            answer.append(str(i))
    return answer
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
    pass


def t7(lst):
    summa = 0
    for i in lst:
        if lst.count(i) == 1:
            summa += i
    return summa
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    pass


def t8(string):
    import re
    rexp = r'[0-9]+'
    answ = re.findall(rexp, string)
    for i in answ:
        i = int(i)
    return max(answ)
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    pass


def t9(number):
    return ('{:05}'.format(number))
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    pass


def t10(string):
    d = {'R R': 'R', 'G G': 'G', 'B B': 'B', 'B G': 'R', 'G B': 'R', 'R G': 'B', 'G R': 'B', 'B R': 'G', 'R B': 'G'}

    def ff(string):
        new_string = str()
        sp = string.split(' ')
        for k in range(1, len(sp)):
            key = " ".join([sp[k - 1], sp[k]])
            new_string += d[key] + ' '
        return new_string[:-1]

    def outer(string):
        print(string)
        for i in range(len(string) - 1):
            string = ff(string)
        return string

    outer(string)
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
    lst = str(lst)
    rexp = r'[0-9]+'
    answ = re.findall(rexp, lst)
    return answ
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    pass


def t13(number_1, number_2):
    number_1 = str(number_1)
    number_2 = str(number_2)
    list1 = [i for i in filter(str.isdigit, number_1)]
    list2 = [j for j in filter(str.isdigit, number_2)]

    list3 = [int(k) for k in list1]
    list4 = [int(q) for q in list2]

    c = [x + y for x, y in zip(list3, list4)]
    for i in range(len(c)):
        c[i]=str(c[i])
    answer = ''.join(c)
    return answer
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    pass


def t14(string):
    dict = {'+': 'Plus',
            '-': 'Minus',
            '*': 'Times',
            '/': 'Divided By',
            '**': 'To The Power Of',
            '=': 'Equals',
            '!=': 'Does Not Equal', '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10':'Ten'}
    s=string.split()
    return dict.get(s[0])+' '+dict.get(s[1])+' ' +dict.get(s[2])
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
    l = []
    sum1 = 0
    sum2 = 0
    for i in m:
        for j in range(len(lst)):
            l.append(i[j])
    for k in range(0, len(lst) ** 2, len(lst) + 1):
        sum1 += l[k]
    for q in range(len(lst) - 1, len(lst) ** 2 - len(lst) + 1, len(lst) - 1):
        sum2 += l[q]
    return sum1 + sum2
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    pass

