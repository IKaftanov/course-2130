def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    if number%20 == 0:
        return number
    else: return 20*(number//20 + 1)


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    return string[::-1]


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    return str(dictionary).strip('{}').replace('\'', '').replace(',', ';')


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return sub_string[::-1] in string



def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    
    Работает только если внутри строки есть пробелы до и после числа. Без этого нужны регулярки
    """
    special_strings = []
    for string in strings:
        numbers = [int(s) for s in string.split() if s.isdigit()]
        if len(numbers) == 4:
            if numbers[3] == numbers[0]*numbers[1]*numbers[2]:
                special_strings.append(string)
    return special_strings