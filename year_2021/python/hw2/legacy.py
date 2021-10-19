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
    string_list = string.split(' ')
    return ' '.join([x[::-1] for x in string_list])


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    import json
    return json.dumps(dictionary).replace("{", "").replace("}", "").replace("'", "").replace('"', "").replace(',', ";")


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return (sub_string[::-1] in string)



def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    import re
    pattern = re.compile('\d+ \d+ \d+ \d+\*\d+\*\d+')
    match = [x for x in strings if pattern.match(x)]
    filtered_matched = []
    for i in match:
        x, y, z = re.findall('\d+ ', i)
        pattern = re.compile('.*{}\*{}\*{}.*'.format(x.replace(' ', ''), y.replace(' ', ''), z.replace(' ', '')))
        if pattern.match(i):
            filtered_matched.append(i)
    return filtered_matched