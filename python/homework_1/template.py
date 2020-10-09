def t1(number):
	return (number+19) // 20 *20
	
def t2(string):
    return ' '.join(string[::-1].split()[::-1])
	
def t3(dictionary):
    return '; '.join(f'{k}: {v}' for k, v in dictionary.items())

def t4(string, sub_string):
    return sub_string[::-1] in string
	
def t5(strings):
    s = []
    for string in strings:
        try:
            x, y, z = [int(i) for i in string.split()[:3]]
            if (f'{x} {y} {z} {x*y*z}' == string)and(x>=0)and(y>=0)and(z>=0):      
                s.append(string)
        except:
            continue
    return s

def t6(string):
    while string.find('#') >= 0:
        i = string.find('#')
        string = string[:max(0,i-1)]+string[i+1:]
    return string

def t7(lst):
    return sum([x for x in set(lst) if lst.count(x) == 1])
	
import re
def t8(string):
    return max(map(int,re.findall(r'\d+', string)))

def t9(number):
    return f'{number:05d}'
	
def t10(string):
    d = {"GG": "G", "BG": "R", "RG": "B", "BR": "G", "GB": "R", "GR": "B", "RB": "G", "RR": "R", "BB": "B"}
    while len(string) > 1:
        s = ""
        for i in range(len(string)-1):
            s = s+d.get(string[i:i+2])
        string = s
    return string

def t11(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return i  
    return int(-1)
	
def t12(lst):
    ns = []
    for string in lst:
        n = ''.join(re.findall(r'\d+', string))
        ns.append(n[0].replace('7', '8')+n[1:])    
    return ns
	
def t13(number_1, number_2):
    s=''
    while max(number_1, number_2) > 0:
        s= str(number_1 % 10 + number_2 % 10) + s
        number_1 = number_1 //10
        number_2 = number_2 //10
    if s != '':
        return int(s)
    return int(0)
	
def t14(string):
    d = { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ',
          '1':   'One', 
          '2':  'Two', 
          '3':  'Three', 
          '4':  'Four', 
          '5':  'Five', 
          '6':  'Six', 
          '7':  'Seven', 
          '8':  'Eight', 
          '9':  'Nine', 
          '10': 'Ten'}
    for i in set(string.split()):
        string = string.replace(i, d.get(i))
    return ' '.join(string.split())
	
def t15(lst):
    s = 0
    i = 0
    for raw in lst:
        s += raw[i] + raw[-(1-i)]
        i +=1
    return s
