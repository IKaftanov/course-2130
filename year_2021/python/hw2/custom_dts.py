#from __future__ import annotations
from typing import List, Any


class CycledList:
    """
    Реализуйте список фиксированой длины, в котором новые элементы перезаписываются
    ```
    cycled_list = CycledList(5)
    cycled_list.append(1)
    cycled_list.append(2)
    cycled_list.append(3)
    cycled_list.append(4)
    cycled_list.append(5)
    cycled_list.append(6)
    ```
    Expected Output:
    ```
    [6, 2, 3, 4, 5]
    ```
    """
    def __init__(self, size: int):
        self._data = []
        self._size = size

    def append(self, item):
        if len(self._data) == self._size:
            self._data[0] = item
        else:
            self._data.append(item)

# проверка
cycled_list = CycledList(5)
cycled_list.append(1)
cycled_list.append(2)
cycled_list.append(3)
cycled_list.append(4)
cycled_list.append(5)
cycled_list.append(6)

#print(cycled_list._data)

class Fraction:
    """
    Написать класс чисел с бесконечной точностью. Дроби.
    Определите следующие операции:
    1. a / b
    2. a + b
    3. a * b
    4. a - b
    Вы можете найти больше здесь https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
    В каждый момент времени дробь должна быть правильной
    """

    def __init__(self, nominator, denominator):
        # с учётом упрощения, если есть общие делители
        import math
        self.nominator = nominator//math.gcd(nominator, denominator)
        self.denominator = denominator//math.gcd(nominator, denominator)

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)

    def __add__(self, other):
        return Fraction(self.nominator * other.denominator + self.denominator * other.nominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.nominator * other.denominator - self.denominator * other.nominator, self.denominator * other.denominator)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'

    # иначе одинаковые дроби не считаются одинаковыми
    def __eq__(self, other) -> bool:
        if (self.nominator == other.nominator) and (self.denominator == other.denominator):
            return True
        else:
            return False

# проверка
a = Fraction(9, 6)
b = Fraction(3, 2)
#print(a == b)
#print(a+b)
#print(a/b)
#print(a*b)

class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter
    Достаточно поддерживать только два метода
    """

    def __init__(self, iterable):
        self._data = {x: iterable.count(x) for x in iterable}

    def append(self, item):
        if item in self._data:
            self._data[item] = self._data[item] + 1
        else:
            self._data[item] = 1

    def remove(self, item):
        del self._data[item]

# проверка
counter_list = MyCounter(['a', 'a', 'b', 'c'])
#print(counter_list._data)
counter_list.append('c')
#print(counter_list._data)
counter_list.remove('a')
#print(counter_list._data)

class Figure:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        return None

    def square(self):
        return None

    def __repr__(self):
        return f'Figure({self.name})'


class Square(Figure):
    """
    Реализуйте класс квадрат и два метода для него
    """
    def __init__(self, a, b):
        self.name = 'Square'
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

# проверка
squared = Square(10, 10)
print(squared.perimeter())
print(squared.square())

import json
class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл
    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self._iterable = iterable
        self._path_to_file = path_to_file
        with open(self._path_to_file, "w+") as fp:
            json.dump(self._iterable, fp)

    def append(self, appended: List[Any]):
        self._iterable.append(appended)
        with open(self._path_to_file, "w+") as fp:
            json.dump(self._iterable, fp)

    def __getitem__(self, item):
        return self._iterable[item]

    def delete(self, key):
        key = key % len(self._iterable)
        del self._iterable[key]
        with open(self._path_to_file, "w+") as fp:
            json.dump(self._iterable, fp)

    def __repr__(self):
        return f'{self._iterable}'

# проверка
pers_list = PersistentList(['a', 'b', 'f', 'd'], 'output.csv')
pers_list.append(['g','hd'])
#print(pers_list._iterable)
#print(pers_list.__getitem__(2))
pers_list.delete(1)
#print(pers_list.__getitem__(1))
