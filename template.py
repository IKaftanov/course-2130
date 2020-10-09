import requests

class WeatherAPI:
    # https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test-docpage/#req-example
    api_key = {}
    api_url = 'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&extra=true'
    response = requests.get(api_url, headers=api_key)
    data = response.json()
    fact = data['fact']
    info = data['info']
    forecasts = data['forecasts']
    dt_now = datetime.now()

    def __init__(self, api_key):
        pass

    def get_current_weather(self, lat, lon):

        print(dt_now.strftime('%d.%m.%Y %H:%M'))
        print('time zone name', info['tzinfo']["name"])
        print('description :', fact['condition'])
        print('Temperature :', fact['temp'], 'degrees Celsius')
        print('Wind speed:', fact['wind_speed'], 'm/s')

        pass

    def get_forecast(self, lat, lon):
        for i in range(0, 7):
            print('Date:', forecasts[i]["date"])
            t1 = forecasts[i]["parts"]["night"]["temp_avg"]
            t2 = forecasts[i]["parts"]["day"]["temp_avg"]
            t3 = forecasts[i]["parts"]["morning"]["temp_avg"]
            t4 = forecasts[i]["parts"]["evening"]["temp_avg"]
            print("average temp:", (t1 + t2 + t3 + t4) / 4)

            print('night condition', forecasts[i]["parts"]["night"]["condition"])
            print('morning condition', forecasts[i]["parts"]["morning"]["condition"])
            print('day condition', forecasts[i]["parts"]["day"]["condition"])
            print('evening condition', forecasts[i]["parts"]["evening"]["condition"])
            print('sunrise:', forecasts[i]["sunrise"])
            print('sunset:', forecasts[i]["sunset"])

        pass



def t1(number):
    a = int(number)
    b = (1 + a // 20) * 20
    return b
    pass


def t2(string):
    b = list(string)
    b.reverse()
    c = ("".join(b))
    if len(a) == 0:
        return '""'
    else:
        return str(c)
    pass

def t3(dictionary):
    if dictionary=={}:
        return '""'
    else:list1 = []
    for key, value in dictionary.items():
        res = key + ": " + str(value)
        list1.append(res)
        r = "; ".join(list1)
    return r
    pass

def t4(string, sub_string):
    s = string
    t = sub_string
    t = t[::-1]
    result = t in s
    return result
    pass


def t5(strings):
    l = []
    for i in strings:
        x = i.split(" ")
        a = int(x[0])
        b = int(x[1])
        c = int(x[2])
        d = int(x[3])
        if d == a * b * c:
            l.append(i)
    return l
    pass


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
    if b == "":
        return '""'
    else:
        return b
    pass

    
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
    pass


def t8(string):
    s = string
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
    listOfNumbers = [float(i) for i in newstr.split()]
    maxs = int(max(listOfNumbers))
    return maxs
    pass


def t9(number):
    num1 = number
    num1 = int(num1)
    fnum1 = "{:0>5d}".format(num1)
    return str(fnum1)
    pass


def t10(string):
   
    x = string
    s = {"B", "G", "R"}
    i = 0
    if len(x) == 1:
        a = x[0]
    else:
        while i < len(x) - 1:
            if x[i] == x[i + 1]:
                a = x[i]
            else:
                s.remove(x[i])
                s.remove(x[i + 1])
                a = "".join(s)
            i += 1
            s = {"B", "G", "R"}

    return a
    pass


def t11(lst):
    l = lst
    l = list(l)
    a = sum(l)
    c = 0
    for i, j in enumerate(l):
        if 2 * c < a:
            c = c + j
        else:
            if 2 * c - l[i - 1] == a:
                return (i - 1)
            else:
                return -1

    pass


def t12(lst):
    import re
    s = lst
    s = str(s)
    r = re.findall(r'\d+', s)
    a = "".join(r)
    a = [a[i:i + 11] for i in range(0, len(s), 11)]
    a = filter(None, a)
    return a
    pass


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
    pass


def t14(string):
    s = string
    d = {'+': 'Plus ',
         '-': 'Minus ',
         '*': 'Times ',
         '/': 'Divided By ',
         '**': 'To The Power Of ',
         '=': 'Equals ',
         '!=': 'Does Not Equal ',
         '0': 'zero',
         '1': 'one',
         '2': 'two',
         '3': 'three',
         '4': 'four',
         '5': 'five',
         '6': 'six',
         '7': 'seven',
         '8': 'eight',
         '9': 'nine'}
    l = list(d.keys())
    for i in l:
        s = s.replace(i, d[i])
    return s
    pass


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
    pass


