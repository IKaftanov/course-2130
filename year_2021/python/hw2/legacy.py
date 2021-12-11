def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number%20!=0:
        number+=1
    pass


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    string_split = string.split()
    string=''
    for j in range(len(string_split)):
        if j+1 == len(string_split):
            string +=string_split[j-1][::-1]
        else:
            string +=string_split[j-1][::-1]+' '
    pass


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    dictionary = ''
    for i in range(len(values)):
        if i+1 == len(values):
            dictionary +=keys[i-1]+': '+str(values[i-1])
        else:
            dictionary +=keys[i-1]+': '+str(values[i-1])+'; '
    pass


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    sub_string = sub_string[::-1]
    string.find(sub_string) != -1
    pass


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass
