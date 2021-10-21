def t1(number):
    x = number - number%20 + 20
    return x
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """


def t2(string):
    x = string.split()
    y = ""
    for i in range(len(x)):
        z = x[i][::-1]
        y += " "
        y += z
    return y[1::]
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    pass


def t4(string, sub_string):
    x = sub_string in string
    return x
    
    """
    проверить есть ли в строке инвертированная подстрока
    """
    


def t5(strings):
    x = []
    for i in range(len(strings)):
        if len(strings[i].split()) == 4:
            if int(strings[i].split()[0])*int(strings[i].split()[1])*int(strings[i].split()[2]) == int(strings[i].split()[3]):
                x.append(strings[i])
    return x
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass