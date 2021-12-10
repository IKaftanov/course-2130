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
        self.element_number = 0
    def append(self, item):
        if self.size > len(self._data):
            self._data.append(item)
        else:
            self._data[self.element_number] = item
            if self.element_number < self.size - 1:
                self.element_number += 1
            else:
                self.element_number = 0

        pass


def gcd(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)
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
        self.nominator = self.nominator*other.denominator
        self.denominator = self.denominator*other.nominator
        return self

    def __add__(self, other):
        self.nominator = self.nominator*other.denominator +self.denominator*other.nominator
        self.denominator = self.denominator*other.denominator
        return self
    def __mul__(self, other):
        self.nominator = self.nominator*other.nominator
        self.denominator = self.denominator*other.denominator
        return self
    def __sub__(self, other: Fraction) -> Fraction:
        self.nominator = self.nominator * other.denominator - self.denominator * other.nominator
        self.denominator = self.denominator * other.denominator
        return self
    def __eq__(self, other):
        if (self.nominator/ gcd(self.nominator, self.denominator) == other.nominator/ gcd(other.nominator, other.denominator)
            and self.denominator/ gcd(self.nominator, self.denominator) == other.denominator/ gcd(other.nominator, other.denominator)):
            return True
        else:
            return False
    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'



class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self._data = None
        counter = {}
        for item in iterable:
            counter[item] = counter.get(item, 0) + 1
        self._data = counter
    def append(self, item):
        if item in self._data:
            self._data += 1
        else:
            self._data[item] = 0

    def remove(self, item):
        if item in self._data:
            del self._data[item]

class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 4* self.a

    def square(self):
        return self.a ** 2

    def __repr__(self):
        return f'Figure({self.name})'


class Square(Figure):
    """
    Реализуйте класс квадрат и два метода для него
    """
    pass


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.obj = iterable
        self.path = path_to_file
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.obj))

    def append(self, item):
        self._item = item
        self._iterable.append (self._item)
        with open (self.path, 'w') as file:
            json.dum (self._iterable, file )

    def __getitem__(self, index):
        """ return item by index """
        with open (self.path, 'w') as f:
            json.dump(self.obj, f)

    def __delitem__(self, index: int) -> None:
        """ delete item by index
                   if index greater then length of list back to start and repeat
                       [1, 2, 3] -> delete(4) -> [1, 3]
                   if index lower then delete from end of list
               """
    def __repr__(self):
        pass