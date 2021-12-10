  Пример: -5 -> 0
    """
    pass
    if number % 20 == 0:
        return number
    else:
        if number < 0:
            return (int(number/20)*20)
        else:
            return (int(number/20)*20 + 20)
            
            
            
def t2(string):
	
    Пример: `abc abc abc` -> `cba cba cba`
    """
    pass
    lst = []
    str_splitted = string.split(' ')
    for i in str_splitted:
        lst.append(i[::-1])
    return (' '.join(lst))


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    pass
    str_new = ''
    k = 0

    for key, value in dictionary.items():
        if k == len(dictionary) - 1:
            str_new = str_new + f'{key}: {value}'
        else:
            str_new = str_new + f'{key}: {value}; '
            k += 1
    return str_new


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    pass
    if string[::-1].find(sub_string) != -1:
        return True
    else:
        return False


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass
