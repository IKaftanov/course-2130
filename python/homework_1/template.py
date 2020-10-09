"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    if number%20 == 0 : new = number
    else: new = (number//20+1)*20 
    return new
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    pass


def t2(string):
    new = ' '.join(i[::-1] for i in string.split(' '))
    return new
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    pass


def t3(dictionary):
    new = '; '.join([f'{key}: {value}' for key, value in dictionary.items()])
    return new
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    pass


def t4(string, sub_string):
    if string.find(sub_string[::-1])==-1: new = False 
    else: new = True 
    return new
    """
    проверить есть ли в строке инвертированная подстрока
    """
    pass


def t5(strings):
    new = []
    for i in range(len(strings)):
        if strings[i].replace(' ', '').isdigit() == 1: 
            k= [int(j) for j in strings[i].split(" ")]
            if k[3]==k[0]*k[1]*k[2] and len(k)==4: new.append(strings[i])
            else: i=i+1
    return new
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    pass


def t6(string):
       while string.find("#")!=-1:
        if string.find("#")==0 : string = string[string.find("#")+1:]
        else: string = string[:(string.find("#")-1)]+string[(string.find("#")+1):]
    return string
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    pass


def t7(lst):
    new = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                break
        else: new.append(lst[i])
    return sum(new)
    
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    pass


def t8(string):
    new=[] 
    num='' 
    for i in range(len(string)): 
        if string[i].isdigit()==1: num=num+string[i] 
        else: 
            if num!='': 
                new.append(int(num)) 
                num='' 
    if num!='': 
        new.append(int(num)) 
    return max(new)
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    pass


def t9(number):
    if len(str(num))>4: return str(num)
    else: return str(num).replace(str(num),(5-len(str(num)))*'0'+str(num))
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    pass

def t10(string):
    while len(string)>1:
            string = string.split(' ')
            string = ' '.join([string[i]+string[i+1] for i in range(len(string)-1)])
            string = string.replace('GG','G').replace('RR','R').replace('BB','B').replace('GB','R').replace('BG','R').replace('RB','G').replace('BR','G').replace('GR','B').replace('RG','B')
    else: return string
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """
    pass


def t11(lst):
    l = []
    for i in range(1,len(lst)-1):
        if lst[i-1]==lst[i+1]: l.append(i)
        else: i+1
    return min(l)
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    pass


def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    pass


def t13(number_1, number_2):
    j=str(max(number_1,number_2))[:len(str(max(number_1,number_2)))-len(str(min(number_1,number_2)))]
    new = []
    for i in range(len(str(min(number_1,number_2)))):
        new.append(str(int(str(number_1)[-i-1])+ int(str(number_2)[-i-1])))
    new = new[::-1]  
    new = j + ''.join(new)
    return new
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    pass


def t14(string):
    def t14(string): 
    symb={ '+': 'Plus ', '-': 'Minus ', '*': 'Times ', '/': 'Divided By ', '**': 'To The Power Of ', '=': 'Equals ', '!=': 'Does Not Equal ' } 
    num={'10': 'Ten ', '9': 'Nine ','8': 'Eight ','7': 'Seven ','6': 'Six ','5': 'Five ','4': 'Four ','3': 'Three ','2': 'Two ','1': 'One ', '0': 'Zero '} 
    symb.update(num) 
    c=string.split() 
    for i in range(len(c)): 
        c[i]=symb[c[i]] 
    return ''.join(c).strip()
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    pass


def t15(lst):
    st = len(lst)
    col = len(lst[1])
    new=[]
    for i in range(st):
        for j in range(col):
            if i == j and i!=col -1 -i : new.append(lst[i][j] )
            elif j == col -1 -i and i!=col -1 -i: new.append(lst[i][j])
            elif i == j and j == col -1 -i: 
                new.append(lst[i][j])
                new.append(lst[i][j])
            else: j+1
    return(sum(new))
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    pass

