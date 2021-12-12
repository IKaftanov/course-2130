from __future__ import annotations
from typing import List, Any
from math import gcd
import json
from collections.abc import Iterable


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
        self.size = size
        self.pos = 0

    def append(self, item):
        if len(self._data) < self.size :
            self._data.append(item)
        else :
            self._data[self.pos] = item            
            self.pos = self.pos + 1 if self.pos < len(self._data) - 1 else 0


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
        self.nominator = int(nominator / gcd(nominator, denominator))
        self.denominator = int(denominator / gcd(nominator, denominator))

    def __truediv__(self, other):
        nom = self.nominator * other.denominator
        denom = self.denominator * other.nominator
        return Fraction(nom, denom)

    def __add__(self, other):
        nom = self.nominator * other.denominator + self.denominator * other.nominator
        denom = self.denominator * other.denominator
        return Fraction(nom, denom)

    def __mul__(self, other):
        nom = self.nominator * other.nominator
        denom = self.denominator * other.denominator
        return Fraction(nom, denom)

    def __sub__(self, other: Fraction) -> Fraction:
        nom = self.nominator * other.denominator - self.denominator * other.nominator
        denom = self.denominator * other.denominator
        return Fraction(nom, denom)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'
    
    def __eq__(self, other): 
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.nominator == other.nominator and self.denominator == other.denominator


class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter
    Достаточно поддерживать только два метода
    """

    def __init__(self, iterable):
        self._data = dict()
        for elem in iterable :
            if elem in self._data.keys() :
                self._data[elem] += 1
            else :
                self._data[elem] = 1

    def append(self, item):
        if item in self._data.keys() :
            self._data[item] += 1
        else :
            self._data[item] = 1

    def remove(self, item):
        del self._data[item]


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
        self.a = a
        self.b = b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def square(self):
        return self.a * self.b


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл
    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.obj = iterable
        self.path = path_to_file
        
        with open(self.path, 'w') as f :
            f.write(json.dumps(self.obj))
            
    def __getitem__(self, key):
            return self.obj[key]
    
    def delete(self, key):
        if key > len(self.obj) - 1 :
            del self.obj[key // len(self.obj)]
        else :
            del self.obj[key]
        
        with open(self.path, 'w') as f :
            f.write(json.dumps(self.obj))

    def append(self, item):
        self.obj.append(item)
        
        with open(self.path, 'w') as f :
            f.write(json.dumps(self.obj))
            
    def __repr__(self):
        return str(self.obj)