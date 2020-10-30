
def t1(number):
    if number%20 == 0 : 
        new = number
    else:
        new = (number//20+1)*20 
    return new



def t2(string):
    new = ' '.join(i[::-1] for i in string.split(' '))
    return new




def t3(dictionary):
    new = '; '.join([f'{key}: {value}' for key, value in dictionary.items()])
    return new




def t4(string, sub_string):
    if string.find(sub_string[::-1])==-1:
        new = False 
    else: 
        new = True 
    return new



def t5(strings):
    new = []
    for i in range(len(strings)):
        if strings[i].replace(' ', '').isdigit() == 1: 
            k= [int(j) for j in strings[i].split(" ")]
            if k[3]==k[0]*k[1]*k[2] and len(k)==4:
                new.append(strings[i])
            else: i=i+1
    return new




def t6(string):
    while string.find("#")!=-1:
        if string.find("#")==0 :
            string = string[string.find("#")+1:]
        else:
            string = string[:(string.find("#")-1)]+string[(string.find("#")+1):]
    return string




def t7(lst):
    new = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                break
        else:
            new.append(lst[i])
    return sum(new)
    




def t8(string):
    new=[]
    num=''
    num1=''
    for i in range(len(string)): 
        num1=num
        num=num+string[i]
        if num.isdigit()!=1:
            num=''
            if num1!='':
                new.append(int(num1))
                num1=''
    new.append(int(num))
    return max(new)

  

def t9(number):
    if len(str(number))>4:
        return str(number)
    else:
        return str(number).replace(str(number),(5-len(str(number)))*'0'+str(number))



def t10(string):
    b = list(string)
    c=len(b)
    e=''
    if c==1:
        return ''.join(b)
    for i in range(c-1):
        d=len(b)
        e=''
        for j in range(d-1):
            if (b[j]=='B' and b[j+1]=='R') or (b[j+1]=='B' and b[j]=='R'):
                e=e+'G'
            elif (b[j]=='R' and b[j+1]=='G') or (b[j+1]=='R' and b[j]=='G'):
                e=e+'B'
            elif (b[j]=='G' and b[j+1]=='B') or (b[j+1]=='G' and b[j]=='B'):
                e=e+'R'
            else:
                e=e+b[j]
        b = list(e)
    return ''.join(b)
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
  


def t11(lst):
    l = []
    for i in range(1,len(lst)-1):
        if sum(lst[:i])==sum(lst[i+1:]): 
            l.append(i)
        else:
            i+1
    if l==[]:
        l.append(-1)
    else:
        l
    return min(l)
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    pass


import re
def t12(lst):
    b=[]
    d=[]
    for i in range(len(lst)):
        a=''.join(re.findall(r'\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}',lst[i]))
        c=list(a)
        d=[]
        for j in range(len(c)):
            if c[j].isdigit()==1:
                d.append(c[j])
        d=''.join(d)
        if len(d)==11:
            d='8'+d[1::]
        else: d='8'+d
        b.append(d)
    return b

    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
 


def t13(number_1, number_2):
    j=str(max(number_1,number_2))[:len(str(max(number_1,number_2)))-len(str(min(number_1,number_2)))]
    new = []
    for i in range(len(str(min(number_1,number_2)))):
        new.append(str(int(str(number_1)[-i-1])+ int(str(number_2)[-i-1])))
    new = new[::-1]  
    new = j + ''.join(new)
    return int(new)
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """




def t14(string):
    dicti={ '+':   'Plus', '-':   'Minus', '*':   'Times', '/':   'Divided By', '**':  'To The Power Of', '=':   'Equals', '!=':  'Does Not Equal', '10': 'Ten', '9': 'Nine','8': 'Eight','7': 'Seven','6': 'Six','5': 'Five','4': 'Four','3': 'Three','2': 'Two','1': 'One', '0': 'Zero' }
    s=string.split()
    for i in range(len(s)):
        s[i]=dicti[s[i]]
    return ' '.join(s)
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



def t15(lst):
    st = len(lst)
    col = len(lst[0])
    new=[]
    for i in range(st):
        for j in range(col):
            if i == j and i!=col -1 -i :
                new.append(lst[i][j] )
            elif j == col -1 -i and i!=col -1 -i:
                new.append(lst[i][j])
            elif i == j and j == col -1 -i: 
                new.append(lst[i][j])
                new.append(lst[i][j])
            else: 
                j+1
    return(sum(new))
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """


