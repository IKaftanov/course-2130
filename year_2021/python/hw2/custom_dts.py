from __future__ import annotations
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
        self.size = size
        self.index = 0

    def append(self, item):
        if len(self._data) < self.size:
            self._data.append(item)
        else:
            self._data[self.index] = item
            self.index += 1 if self.index < self.size - 1 else 0
        pass


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
        self.nominator = nominator
        self.denominator = denominator
        max = 1
        for i in range(2, min(self.nominator, self.denominator) + 1):
            if self.nominator % i == 0 and self.denominator % i == 0:
                max = i
        self.nominator = self.nominator // max
        self.denominator = self.denominator // max

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)
        pass

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.nominator + other.nominator, self.denominator)
        else:
            return Fraction(self.nominator * other.denominator + other.nominator * self.denominator,
                            self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator * other.denominator)
        pass

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.nominator - other.nominator, self.denominator)
        else:
            return Fraction(self.nominator * other.denominator - other.nominator * self.denominator,
                            self.denominator * other.denominator)
        pass

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
        for i in iterable:
            self._data[i] = self._data.get(i, 0) + 1

    def append(self, item):
        self._data[item] = self._data.get(item, 0) + 1

    def remove(self, item):
        self._data.pop(item)


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

    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def square(self):
        return self.a ** 2
    pass


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        pass

    def append(self):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass

    def __repr__(self):
        pass
