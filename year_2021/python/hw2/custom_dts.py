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
        self._size = size
        self.element = 0

    def append(self, item):
        if len(self._data) == self._size:
            self._data[self.element] = item
            self.element += 1
            if self.element >= self._size:
                self.element = 0
        else:
            self._data.append(item)


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
        self.reduction()

    def reduction(self):
        nominator = self.nominator
        denominator = self.denominator
        while (nominator != 0) and (denominator != 0):
            if nominator >= denominator:
                nominator = nominator % denominator
            else:
                denominator = denominator % nominator
        gcd = denominator + nominator
        self.nominator //= gcd
        self.denominator //= gcd

    def __truediv__(self, other):
        inverted_other = Fraction(other.denominator, other.nominator)
        return self * inverted_other

    def __add__(self, other):
        first_nominator = self.nominator * other.denominator
        first_denominator = self.denominator * other.denominator
        second_nominator = other.nominator * self.denominator
        return Fraction(first_nominator + second_nominator, first_denominator)

    def __mul__(self, other):
        nominator = self.nominator * other.nominator
        denominator = self.denominator * other.denominator
        return Fraction(nominator, denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        first_nominator = self.nominator * other.denominator
        first_denominator = self.denominator * other.denominator
        second_nominator = other.nominator * self.denominator
        return Fraction(first_nominator - second_nominator, first_denominator)

    def __eq__(self, other):
        return (self.nominator == other.nominator) and (self.denominator == other.denominator)

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
            self.append(i)

    def append(self, item):
        if item in self._data:
            self._data[item] += 1
        else:
            self._data[item] = 1

    def remove(self, item):
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
    def __init__(self, first_storona, second_storona):
        self._first_storona = first_storona
        self._second_storona = second_storona
        super().__init__('Kirill')

    def perimeter(self):
        return 2 * self._first_storona + 2 * self._second_storona

    def square(self):
        return self._first_storona * self._second_storona



class Container:
    def __init__(self, data):
        self.data = data

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, item):
        return self.data[item]

    def append(self, item):
        self.data.append(item)


class PersistentList:
    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """
    def __init__(self, iterable: List[Any], path_to_file: str):
        self._iterable = iterable
        self._path_to_file = path_to_file
        self.write_store()

    def write_store(self):
        with open(self._path_to_file, 'w') as file:
            json.dump(self._iterable, file)

    def append(self, iterable):
        self._iterable.append(iterable)
        self.write_store()

    def __getitem__(self, item):
        return self._iterable.__getitem__(item)

    def delete(self, index: int) -> None:
        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """
        if index > 0:
            index = index % len(self._iterable)
        else:
            index = -(-index % len(self._iterable))
        del self._iterable[index]
        self.write_store()

    def __repr__(self):
        return self._iterable.__repr__()
