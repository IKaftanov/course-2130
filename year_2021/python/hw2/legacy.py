def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number%20 != 0:
        number += 1
    return number

# проверка - протестить -5, 0, 20, 21
#print(t1(21))

def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    string = string.split(' ')
    return ' '.join([x[::-1] for x in string])

# проверка
#print(t2("afs lds rew"))

def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    import json
    return json.dumps(dictionary).replace("{", "").replace("}", "").replace("'", "")\
        .replace('"', "").replace(',', ";")
# проверка
#print(t3({1:'x', 2:'y', 3:'z'}))

def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    if sub_string[::-1] in string:
        return True
    else:
        return False

# проверка
#print(t4("32583485dskfj", "jfks"))

def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    import re
    pattern = re.compile('\d+ \d+ \d+ \d+\*\d+\*\d+')
    matched = [x for x in strings if pattern.match(x)]
    perfect_matched = []
    for substr in matched:
        x, y, z = re.findall('\d+ ', substr)
        pattern = re.compile('.*{}\*{}\*{}.*'.format(x.replace(' ', ''), y.replace(' ', ''), z.replace(' ', '')))
        if pattern.match(substr):
            perfect_matched.append(substr)
    return perfect_matched

# проверка
string_list = ['123 32 35 123*32*35', 'dflgkl', '123 32 35 1*3*3']
#print(t5(string_list))