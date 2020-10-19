import re

def t1(number):
    num1 = int(number)
    if num1 % 20 == 0:
        return num1
    else:
        return (1 + num1 // 20) * 20
  
def t2(string):
    b = string.split()
    list=[]
    c = ""
    for i in x:
        res = i[::-1]
        list.append(res)
        c = " ".join(list)
    return c
  

def t3(dictionary):
    r = ""
    list = []
    for key, value in dictionary.items():
        res = key + ": " + str(value)
        list.append(res)
        r = "; ".join(list)
    return r
   

def t4(string, sub_string):
    s = string
    t = sub_string
    t = t[::-1]
    result = t in s
    return result
   

def t5(strings):
    l = []
    for i in strings:
        x = i.split(" ")
        try:
            a = int(x[0])
            b = int(x[1])
            c = int(x[2])
            d = int(x[3])
            if d == a * b * c:
                l.append(i)
        except ValueError:
            pass
    return l
   


def t6(string):
    S = string
    skip = 0
    l = []
    for x in reversed(S):
        if x == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            l.append(x)
    l = l[::-1]
    a = ' '
    b = a.join(l)
    b = str(b)
    b = ''.join(b.split())
    return b
    
    
def t7(lst):
    arr = lst
    arr = list(arr)
    count_dict = {}
    for i in set(arr):
        count_dict[i] = arr.count(i)
    a = count_dict
    list1 = []
    list2 = []
    for k, v in a.items():
        if v == 1:
            list1.append(k)
            list2.append(v)
    a = dict(zip(list1, list2))
    k = list(a.keys())
    s = sum(k)
    return s
   


def t8(string):
    s = string
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
    listOfNumbers = [float(i) for i in newstr.split()]
    maxs = int(max(listOfNumbers))
    return maxs


def t9(number):
    num1 = number
    num1 = int(num1)
    fnum1 = "{:0>5d}".format(num1)
    return str(fnum1)
  

def t10(string):
    mixes = {'BG': 'R', 'RG': 'B', 'BR': 'G', 'GB': 'R', 'GR': 'B', 'RB': 'G'}  
    if len(string) > 1:
        sub_string = []
        for i in range(len(string) - 1):
            x, y = string[i], string[i + 1]
            if x == y:
                sub_string.append(x)
            else:
                sub_string.append(mixes[x + y])
        return t10(''.join(sub_string))
    else:
        return string
   
    
  


def t11(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i  
    return int(-1)

 


def t12(lst):
    pnum = []
    for string in lst:
        n = ''.join(re.findall(r'\d+', string))
        pnum.append(n[0].replace('7', '8')+n[1:])    
    return pnum



def t13(number_1, number_2):
    a = number_1
    b = number_2
    la = list(str(a))
    lb = list(str(b))
    la = list(map(int, la))
    lb = list(map(int, lb))
    lb = list(reversed(lb))
    la = list(reversed(la))
    l = max(len(la), len(lb))
    d = []
    if len(la) > len(lb):
        lb = lb + [0] * int(len(la) - len(lb))
    else:
        la = la + [0] * int(len(lb) - len(la))
    for i in range(0, l):
        sum1 = int(la[i]) + int(lb[i])
        d.append(sum1)
    d = list(reversed(d))
    e = int(str(d).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""))
    return e
   


def t14(string):
    s = string
    d = {'+': 'Plus ',
         '-': 'Minus ',
         '*': 'Times ',
         '/': 'Divided By ',
         '**': 'To The Power Of ',
         '=': 'Equals ',
         '!=': 'Does Not Equal ',
         '0': 'Zero',
         '1': 'One',
         '2': 'Two',
         '3': 'Three',
         '4': 'Four',
         '5': 'Five',
         '6': 'Six',
         '7': 'Seven',
         '8': 'Eight',
         '9': 'Nine'}
    l = list(d.keys())
    for i in l:
        s = s.replace(i, d[i])
    return s
    


def t15(lst):
    l1 = lst
    l1 = list(l1)
    n = len(l1)
    num1 = 0
    for i in range(n):
        for j in range(n):
            a = l1[i]
            b = a[j]

            if i == j:
                num1 += b
    l1.reverse()
    num2 = 0
    for i in range(n):
        for j in range(n):
            a = l1[i]
            b = a[j]

            if i == j:
                num2 += b
    num0 = num1 + num2
    return num0
    


