def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number % 20 != 0:
        number += 1
    return number


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    return ' '.join([s[::-1] for s in string.split(' ')])


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    b = ''
    for key, val in dictionary.items():
        b += f'{key}: {val}; '
    return b[:-2]


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if string.find(sub_string[::-1]) == -1:
        return False
    else:
        return True


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    res = []
    for s in strings:
        space = s.split(' ')
        if len(space) == 4 and space[:3] == space[3].split('*') and sum([item.isdigit() for item in space[:3] if item[0] != '0']) == 3:
            res.append(s)
        else:
            continue
    return res
