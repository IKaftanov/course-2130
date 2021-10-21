def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number%20 != 0:
        number += 1
    return number


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    string = string.split(' ')
    return ' '.join([x[::-1] for x in string])


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    import json
    return json.dumps(dictionary).replace("{", "").replace("}", "").replace('"', "").replace(',', ";")
        


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if sub_string[::-1] in string:
        return True
    else:
        return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    import re
    pattern = re.compile('\d+ \d+ \d+ \d+\*\d+\*\d+')
    matched_str = [i for i in strings if pattern.match(i)]

    full_matched_str = []
    for elem in matched_str:
        x, y, z = re.findall('\d+ ', elem)
        pattern = re.compile('.*{}\*{}\*{}.*'.format(x.replace(' ', ''), y.replace(' ', ''), z.replace(' ', '')))
        if pattern.match(elem):
            full_matched_str.append(elem)
    return full_matched_str