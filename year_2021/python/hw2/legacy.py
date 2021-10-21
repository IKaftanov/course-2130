def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """

    while (number%20!=0):
        number+=1
    return number


def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    word_list = string.split(" ")
    for number, element in enumerate(word_list):
        word_list[number] = element[::-1]
    pass
    return " ".join(word_list)


def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    string = ""
    for key, value in dictionary.items(): 
        if string!="":
            string+= "; "
        string = string + str(key) + ": " + str(value) 
    pass
    return string


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    a = (sub_string[::-1] in string)
    return a


def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    output_list = []
    for index, element in enumerate(strings):
        constituents = element.split(" ")
        valid = True 
         # whether element should be excluded or not 
        if (len(constituents)==4):
            numbers = constituents[3].split("*")
            if (len(numbers)==3):
                condition = (numbers[0].isdigit())*(numbers[1].isdigit())*(numbers[2].isdigit())
                if condition:
                    condition_2 = (int(numbers[0]) == int(constituents[0]))*(int(numbers[1]) == int(constituents[1]))*(int(numbers[2]) == int(constituents[2]))
                    if condition_2:
                        pass
                    else:
                        valid*=0
                else:
                    valid*=0
            else:
                valid*=0
        else:
            valid*=0
        if valid:
            output_list.append(element)
    return output_list