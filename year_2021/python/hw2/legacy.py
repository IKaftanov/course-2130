def t1(number):
    """
    Поправьте код, чтобы возвращаемое значение было ближайшим сверху, кратным к 20
    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0
    """
    while number%20!=0:
        number=number+1
    print (number)
def t2(string):
    """
    На вход подается набор слов, разделенных пробелом, инвертируйте каждое слово.
    Пример: `abc abc abc` -> `cba cba cba`
    """
    split_str = string.split (' ')
    list = []
    for element in split_str:
        list.append (element [::-1])
    str='{0}'.format(list)
    a=str.replace ("[","")
    a=a.replace ("]","")
    print (a)
def t3(dictionary):
    """
    На вход подается словарь. Преобразуйте его в строку по следующему шаблону 'key: value; key: value' и так далее
    """
    dict='{0}'.format(dictionary)
    dict1=dict.replace(',',';')
    b=dict1.replace("'","")
    b=b.replace('{',"'")
    b=b.replace('}',"'")
    print(b)
def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    split_str = string.split (' ')
    list = []
    for element in split_str:
        list.append (element [::-1])
    str='{0}'.format(list)
    a=str.replace ("[","")
    a=a.replace ("]","")
    с=a.find (sub_string)
    if с==-1:
        print ('Нет')
    else: print ('Есть')
def t5 (strings):
    list = []
    for element in strings:
        if isinstance(element,int):
            list.append(element)
    import copy
    new_list = copy.copy(list)
    p=1
    for i in range (len(new_list)-1):
        p=new_list[i]*new_list[i-1]
        new_list[i]=p
    list.append (p)
    print(list)
