def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    return (20 - number % 20) + number if number % 20 != 0 else number


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    return ' '.join([i[::-1] for i in string.split(' ')])


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    return '; '.join(str(key) + ': ' + str(value) for key, value in zip(dictionary.keys(), dictionary.values()))


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
    return [i for i in strings if (len(i.split(' ')) == 4)
            and (i.split(' ')[0] + '*' + i.split(' ')[1] + '*' + i.split(' ')[2] == i.split(' ')[3])
            and (i.split(' ')[0].isdigit()) and (i.split(' ')[1].isdigit()) and (i.split(' ')[2].isdigit())]
