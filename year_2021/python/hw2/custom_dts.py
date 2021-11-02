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

    def append(self, item):
        if len(self._data) < self.size:
            self._data.append(item)
        else:
            self._data[len(self._data) % self.size] = item
        return self._data


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
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        self.nominator = int(nominator / gcd(nominator, denominator))
        self.denominator = int(denominator / gcd(nominator, denominator))

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)

    def __add__(self, other):
        return Fraction(self.nominator * other.denominator + self.denominator * other.nominator,
                       self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        return Fraction(self.nominator * other.denominator - self.denominator * other.nominator,
                       self.denominator * other.denominator)
    
    def __eq__(self, other):
        """a == b"""
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
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def perimeter(self):
        return 4 * self.a
    
    def square(self):
        return self.a ** 2


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
        
        self.iterable = iterable
        self.path_to_file = path_to_file
        
        self.save()

    
    def save(self):
        import json
        
        with open(self.path_to_file, 'w') as outfile:
            outfile.write(json.dumps(self.iterable))

    def append(self, obj):
        self.iterable.append(obj)
        
        self.save()


    def __getitem__(self, item):

        self.save()

        return self.iterable[item]

    def delete(self, index: int) -> None:
        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """
        if len(self.iterable) < abs(index)+1:
            index = index%len(self.iterable)
            self.iterable.pop(index)
        else:
            self.iterable.pop(index)
            
        self.save()
        

    def __repr__(self):
        
        self.save()
    
        return  json.dumps(self.iterable, default=lambda x: str(x))
