
from intro import filter_by_indices


def t1(number):
   
    now = number // 20
    now = now * 20
    if now < number:
        now += 20
    return now


def t2(string):
   
    s = list(string)
    tot = len(s)
    print(tot)
    l = 0
    while l < tot:
        while s[l] == ' ':
            l = l + 1
        r = l
        while r < tot and s[r] != ' ':
            r = r + 1
        L = l
        R = r - 1
        while L < R:
            s[L], s[R] = s[R], s[L]
            L = L + 1
            R = R - 1
        l = r
        print(l)
    return ''.join(s)


def t3(dictionary):
    
    s = ''
    for key in dictionary:
        s = s + key.__str__() + ': ' + dictionary[key].__str__() + '; '
    return s
    pass


def t4(string, sub_string):
    
    sub = list(sub_string)
    sub.reverse()
    sub = ''.join(sub)
    return sub in string


def t5(strings):
    

    def check(s):
        tot = len(s)
        if tot != 8:
            return False
        if s[4] != '*':
            return False
        if s[6] != '*':
            return False
        if s[0] != s[3]:
            return False
        if s[1] != s[5]:
            return False
        if s[2] != s[7]:
            return False
        return s[0].isdigit() and s[1].isdigit() and s[2].isdigit()

    lst = []
    now = 0
    for str in strings:
        ss = str.split(' ')
        if not check(ss):
            lst.append(now)
        now = now + 1
    filter_by_indices(strings, lst)
    pass


m = {1: 2, 3: 3, 4: 5}

print(t1(21))
print(t2('abc abc abc'))
print(t3(m))
print(t4('abc abc abc', 'abc'))


l = []
l.append('12 13 14 ')

