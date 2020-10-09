#!/usr/bin/env python
# coding: utf-8

# In[32]:


"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


# In[90]:


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    return((number - 1) // 20 * 20 + 20)
    pass


# In[103]:


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    arr = string.split(' ')
    n = len(arr)
    i = 0
    s = ""
    for a in arr:
        i = i + 1
        s = s + str(a[::-1])
        if i != n:
            s = s + " "
    return(s)
    pass


# In[79]:


def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    n = len(dictionary)
    i = 0
    s = ""
    for k, v in dictionary.items():
        i = i + 1
        s = s + str(k) + ": " + str(v)
        if i != n:
            s = s + "; "
    return(s)
    pass


# In[106]:


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return(sub_string[::-1] in string)
    pass


# In[114]:


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    r = []
    for string in strings:
        a = string.split(' ')
        if int(a[0]) * int(a[1]) * int(a[2]) == int(a[3]):
            r.append(string)
    return(r)
    pass


# In[142]:


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    a = [1 for i in range(len(string))]
    for i in range(len(string)):
        if string[i] == '#':
            a[i] = 0
            j = i
            while (a[j] != 1) and (j != 0):
                j = j - 1
            a[j] = 0
    s = ""
    for i in range(len(string)):
        if a[i] == 1:
            s = s + string[i]
    return(s)
    pass


# In[178]:


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    d = {}
    for i in lst:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    uniq = [i for i in d.keys() if d[i] == 1]
    s = 0
    for el in uniq:
        s = s + el
    return(s)
    pass


# In[182]:


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    n = 0
    maxn = 0
    for i in range(len(string)):
        if string[i].isdigit():
            n = n * 10 + int(string[i])
        else:
            if n > maxn:
                maxn = n
            n = 0
    if n > maxn:
        maxn = n
    return(maxn)
    pass


# In[185]:


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    s = str(number)
    n = ""
    for i in range(5 - len(s)):
        n = n + "0"
    return(n + s)
    pass


# In[208]:


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
    n = len(string)
    a = [[0] * n for i in range(n)]
    for i in range(n):
        if string[i] == "R":
            a[0][i] = 1
        if string[i] == "G":
            a[0][i] = 2
        if string[i] == "B":
            a[0][i] = 3
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[i][j] != a[i][j + 1]:
                a[i + 1][j] = 6 - a[i][j] - a[i][j + 1]
            else:
                a[i + 1][j] = a[i][j]
    if a[n - 1][0] == 1:
        return("R")
    if a[n - 1][0] == 2:
        return("G")
    if a[n - 1][0] == 3:
        return("B")
    pass


# In[215]:


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    s = 0
    for el in lst:
        s = s + el
    sl = lst[0]
    ind = -1
    for i in range(1, len(lst) - 1):
        if sl == s - sl - lst[i]:
            ind = i
            break
        sl = sl + lst[i]
    return(ind)
    pass


# In[291]:


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    import re
    pattern = r'(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){11}(\s*)?'
    delpr = "^\s+|\n|\r|\s+$"
    a = []
    for el in lst:
        res = re.search(pattern, el)
        res.group()
        s = res[0]
        s = re.sub(delpr, '', s)
        i = 1
        if s[0] == '+':
            while s[i] != "7":
                i += 1
            i += 1
        ns = "8"
        while i < len(s):
            if s[i].isdigit():
                ns = ns + s[i]
            i += 1
        a.append(ns)
    return(a)
    pass
t12(["Что-то происходит бла бла бла +7495 123-45-67", "Звони 8 495 123-45-67 мне", "По вопросам рекламы +7(499)123-45-67"])


# In[232]:


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    s = ""
    n1 = len(str(number_1))
    n2 = len(str(number_2))
    for i in range(max(n1, n2)):
        s = str(number_1 % 10 + number_2 % 10) + s
        number_1 //= 10
        number_2 //= 10
    return(int(s))
    pass


# In[242]:


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
    d = { '0':   'Zero ',
          '1':   'One ',
          '2':   'Two ',
          '3':   'Three ',
          '4':   'Four ',
          '5':   'Five ',
          '6':   'Six ',
          '7':   'Seven ',
          '8':   'Eight ',
          '9':   'Nine ',
          '10':   'Ten ',
          '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    s = string.split(" ")
    ns = ""
    for el in s:
        ns = ns + d[el]
    if ns[len(ns) - 1] == " ":
        ns = ns[:len(ns) - 1]
    return(ns)
    pass


# In[219]:


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
        s = s + lst[i][i] + lst[i][len(lst[i]) - 1 - i]
    return(s)
    pass

