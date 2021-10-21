def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    if number%20 == 0:
        return number
    if number>0:
        return number - number%20 + 20
    else:
        return number - number%(-20)

def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    str_s = string.split()
    for i in range(len(str_s)):
        str_s[i] = str_s[i][::-1]
    str_s = ' '.join(str_s)
    return str_s

def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    str1 = str(dictionary)
    str1 = str1.replace("'", "").replace(',', ';')
    return str1[1:-1]


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    string = string[::-1]
    if sub_string in string:
        return True
    else:
        return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass
