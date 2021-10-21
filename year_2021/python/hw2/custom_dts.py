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
        self.i = 0

    def append(self, item):
        if len(self._data) < self.size:
            self._data.append(item)
        else:
            self._data[self.i] = item
            if self.i < self.size - 1:
                self.i += 1
        pass

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator,
                        self.denominator * other.nominator)

    def __add__(self, other):
        return Fraction(self.nominator * other.denominator + self.denominator * other.nominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator,
                        self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator * other.denominator - self.denominator * other.nominator,
                        self.denominator * other.denominator)

    def __eq__(self, other):
        if (self.nominator / gcd(self.nominator, self.denominator) == other.nominator / gcd(other.nominator, other.denominator)
                and self.denominator / gcd(self.nominator, self.denominator) == other.denominator / gcd(other.nominator, other.denominator)):
            return True
        else:
            return False

    def __repr__(self):
        return f'{int(self.nominator / gcd(self.nominator, self.denominator))}/{int(self.denominator / gcd(self.nominator, self.denominator))}'


class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self._data = dict()
        self.iterable = iterable
        for i in self.iterable:
            self._data[i] = self._data.get(i, 0) + 1

    def append(self, item):
        if type(item) is int:
            self._data[item] = self._data.get(item, 0) + 1

        else:
            for i in item:
                self._data[i] = self._data.get(i, 0) + 1
        pass

    def remove(self, item):
        if type(item) is int and item in self._data.keys():
            del self._data[item]
            pass
        elif type(item) is int and item not in self._data.keys():
            pass
        else:
            for i in item:
                if i in self._data.keys():
                    del self._data[i]
                else:
                    continue
            pass


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

    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def perimeter(self):
        return self.length * 4

    def square(self):
        return self.length ** 2


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.iterable = iterable
        self.path_to_file = path_to_file
        with open(self.path_to_file, 'w') as f:
            json.dump(self.iterable, f)

    def append(self, item):
        with open(self.path_to_file) as f:
            self.iterable = json.load(f)

        self.iterable.append(item)

        with open(self.path_to_file, 'w') as f:
            json.dump(self.iterable, f)
        pass

    def __getitem__(self, item):
        with open(self.path_to_file) as f:
            self.iterable = json.load(f)

        return self.iterable[item]

    def delete(self, index: int) -> None:
        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """
        with open(self.path_to_file) as f:
            self.iterable = json.load(f)

        if abs(index) < len(self.iterable):
            del self.iterable[index]
        else:
            index = index - len(self.iterable)
            self.delete(index)

        with open(self.path_to_file, 'w') as f:
            json.dump(self.iterable, f)
        pass

    def __repr__(self):
        pass
