def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number % 20 != 0 :
        number += 1
    return number


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    return ' '.join([s[::-1] for s in string.split()])


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    return '; '.join([f'{k}: {v}' for k, v in dictionary.items()])


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
    out = []
    for string in l :
        new_l = string.split(' ')
        if len(new_l) == 4 :
            x, y, z = new_l[0:3]
            xyz = new_l[-1].split('*')
            try :
                x, y, z = float(x), float(y), float(z)
            except :
                continue
            if x != int(x) or y != int(y) or z != int(z) :
                continue
            if x <= 0 or y <= 0 or z <= 0 :
                continue 
            if len(xyz) == 3 and new_l[0:3] == xyz :
                out.append(string)
    return out