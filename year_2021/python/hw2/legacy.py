def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    if number % 20 != 0:
        delta = 20 - number % 20
        number += delta
    return number


def t2(string):
    """
        На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
        Пример: `abc abc abc` -> `cba cba cba`
    """
    lst = string.split(' ')
    new_lst = []
    for i in range(len(lst)):
        word = lst[i][::-1]
        new_lst.append(word)
    new_string = ' '.join(new_lst)
    return new_string


def t3(dictionary):
    """
        На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    new_lst = []
    for key in dictionary:
        string = (str(key) + ': ' + str(dictionary[key])).strip()
        new_lst.append(string)
    new_string = '; '.join(new_lst)
    return new_string


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    inv_sub = sub_string[::-1]
    if inv_sub in string:
        return True


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    filtered_lst = []
    for string in strings:
        lst = list(map(int, string.split()))
        if lst[0]*lst[1]*lst[2] == lst[3]:
            filtered_lst.append(string)
    return filtered_lst
