from __future__ import annotations
from typing import List, Any


class CycledList:
    _counter = 0
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

    def append(self, item):
        
        if len(self._data)<self.size:
            self._data.append(item)
        else:
            self._data[(CycledList._counter)%self.size] = item
            CycledList._counter += 1
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
        def gcd(m, n):
            while m % n != 0:
                old_m = m
                old_n = n
                m = old_n
                n = old_m % old_n
            return n
        common = gcd(nominator,denominator)
        self.nominator = nominator/common
        self.denominator = denominator/common
        

    def __truediv__(self, other):
        newden = self.denominator*other.nominator
        newnom = self.nominator*other.denominator
            
        return Fraction(newnom, newden)

    def __add__(self, other):
        newnom = self.nominator*other.denominator + self.denominator*other.nominator
        newden = self.denominator * other.denominator
        return Fraction(newnom, newden)

    def __mul__(self, other):
        newnom = self.nominator*other.nominator
        newden=self.denominator*other.denominator
        return Fraction(newnom, newden)

    def __sub__(self, other: Fraction) -> Fraction:
        newnom = self.nominator*other.denominator- self.denominator*other.nominator
        newden = self.denominator*other.denominator
        return Fraction(newnom, newden)

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

    def append(self, item):
        pass

    def remove(self, item):
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
    def __init__(self, side):
        self.side = side
        super().__init__('Square')
        
    def perimeter(self, side):
        return side*4
    def square(self, side):
        return side*side
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
