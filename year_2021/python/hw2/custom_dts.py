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
    k = 0
    end = False

    def __init__(self, size: int):
        self._data = []
        self.size = size

    def append(self, item):
        if self.k < self.size:
            if self.end:
            self._data[self.k] = item
        else:
            self._data.append(item)
            self.k += 1
    else:
        self.k = 0
        self.end = True
        self._data[self.k] = item
        self.k += 1


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
            if(self.nominator % i == 0 and self.denominator % i == 0):
                max = i
        self.nominator = self.nominator // max
        self.denominator = self.denominator // max

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.nominator + other.nominator, self.denominator)
        else:
            return Fraction(self.nominator * other.denominator + self.denominator*other.nominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator*other.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.nominator - other.nominator, self.denominator)
        else:
            return Fraction(self.nominator * other.denominator - self.denominator * other.nominator,
                            self.denominator * other.denominator)

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

        for i in set(iterable):
            count = 0
            for j in range(len(iterable)):
                if iterable[j] == i:
                    count += 1
                    self._data[i] = count

    def append(self, item):
        self._data[item] += 1

    def remove(self, item):
        del (self._data[item])


class Figure:
    def __init__(self,name):
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
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b
    

    


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
        pass

    def append(self, item) -> None:
        """add item to list"""

    def __getitem__(self, index):
        """ return item by index """
        pass

    def delete(self, index: int) -> None:
        """ delete item by index

            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]

            if index lower then delete from end of list

        """

    def __repr__(self):
        pass
