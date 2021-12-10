from __future__ import annotations
from typing import List, Any
import json


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
        self.counter = []

    def append(self, item):
        if len(self._data) < self.size:
            self.counter.append(item)
            self._data.append(item)
        else:
            self.counter.append(item)
            self._data[len(self.counter) % self.size - 1] = item


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
        nom = nominator
        denom = denominator
        while nom % denom != 0:
            old_nom = nom
            old_denom = denom
            nom = old_nom
            denom = old_nom % old_denom
        self.nominator = nominator // denom
        self.denominator = denominator // denom

    def __eq__(self, other):
        if self.nominator == other.nominator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __truediv__(self, other):
        nominator = self.nominator * other.denominator
        denominator = self.denominator * other.nominator
        return Fraction(nominator, denominator)

    def __add__(self, other):
        nominator = self.nominator * other.denominator + other.nominator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __mul__(self, other):
        nominator = self.nominator * other.nominator
        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        nominator = self.nominator * other.denominator - other.nominator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'


class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self._data = {}
        self.append(iterable)

    def append(self, item):
        if hasattr(item, '__iter__'):
            for i in item:
                if i in self._data:
                    self._data[i] += 1
                else:
                    self._data[i] = 1
        else:
            if item in self._data:
                self._data[item] += 1
            else:
                self._data[item] = 1

    def remove(self, item):
        if hasattr(item, '__iter__'):
            for i in item:
                if i in self._data:
                    del self._data[i]
        else:
            if item in self._data:
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
    def __init__(self, name, side):
        super().__init__(name=name)
        self.side = side

    def perimeter(self):
        return self.side * 4

    def square(self):
        return self.side ** 2


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл
    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self._data = []
        self.path = path_to_file
        self.append(iterable)

    def append(self, iterable):
        if self._data:
            self._data.append(iterable)
        else:
            self._data = iterable
        with open(self.path, 'w') as file:
            json.dump(self._data, file)

    def __getitem__(self, item):
        return self._data[item]

    def delete(self, index: int) -> None:
        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """
        if index <= len(self._data):
            del self._data[index]
        else:
            del self._data[index % len(self._data)]
        with open(self.path, 'w') as file:
            json.dump(self._data, file)

    def __repr__(self):
        return f'{self._data}'
