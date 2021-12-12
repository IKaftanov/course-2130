def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    integ = number//20
    if number%20 >0:
        remain = 1
    else:
        remain = 0
        
    return (integ+remain)*20


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
    return str(dictionary).replace(',',';').replace('{','').replace('}','').replace("'","")


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
    ans = [int(s) for s in strings.split() if s.isdigit()]
    
    def multiplyList(myList):
        
        result = 1
        for x in myList:
             result = result * x
        return result
    
    return multiplyList(ans)
