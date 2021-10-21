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
        self.__size = size

    def append(self, value):
        if len(self._data) == self.__size:
            self._data[0] = value
        else:
            self._data.append(value)
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

    def __init__(self, num, denom):

        def gcd(x,y):
            if x > y:
                if x%y!=0:
                    val = gcd(y, x%y)
                else:
                    val = y
            else: 
                if y%x!=0:
                    val = gcd(x, y%x)
                else:
                    val = x
            return val

        div = gcd(num, denom)
        self.num = num//div
        self.denom = denom//div

    
    def __repr__(self):
        return f"{self.num}/{self.denom}"
        

    def __eq__(self, second: Fraction) -> bool:
        return (self.num==second.num)*(self.denom == second.denom)
        

    def __add__(self, second: Fraction) -> Fraction:
        return Fraction(self.num*second.denom+self.denom*second.num, self.denom*second.denom)

    def __sub__(self, second: Fraction) -> Fraction:
        return Fraction(self.num*second.denom-self.denom*second.num, self.denom*second.denom)

    def __mul__(self, second: Fraction) -> Fraction:
        return Fraction(self.num*second.num, self.denom*second.denom)


    def __truediv__(self, second: Fraction) -> Fraction:
        return Fraction(self.num*second.denom, self.denom*second.num)




class MyCounter:

    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self._data = {x: iterable.count(x) for x in iterable}

    def append(self, number):
        if number in self._data:
            self._data[number] = self._data[number] + 1
        else:
            self._data[number] = 1
        pass

    def remove(self, number):
        del self._data[number]
        pass


class Figure:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Figure({self.name})'


    def square(self):
        return None

    def perimeter(self):
        return None


class Square(Figure):

    """
    Реализуйте класс квадрат и два метода для него
    """

    def __init__(self, length, width):
        self.name = 'Square'
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2*self.length + 2*self.width 

    def square(self):
        return self.length*self.width
    
    pass


import json
class PersistentList:

    """
    Реализуйте список где передаваемый список записывается в файл
    Любая операция удаления/добавления должна изменять файл

    Формат файла - json
    """

    
    def __init__(self, iterable: List[Any], path_to_file: str):
        self.path = path_to_file
        self.data = iterable

        with open(path_to_file, "w+") as f:
            json.dump(iterable, f)
        pass


    def __repr__(self):
        return f'{self.data}'

    def __getitem__(self, item):
        item = item % len(self.data)
        return self.data[item]

    def __delitem__(self, key):
        key = key % len(self.data)
        del self.data[key]
        with open(self.path, "w") as f:
            json.dump(self.data, f)
        pass

    def append(self, iterable: List[Any]):
        self.data.append(iterable)
        with open(self.path, "w") as f:
            json.dump(self.data, f)
        pass


    def delete(self, index: int) -> None:

        """ delete item by index
            if index greater then length of list back to start and repeat
                [1, 2, 3] -> delete(4) -> [1, 3]
            if index lower then delete from end of list
        """

        index = index % len(self.data)
        del self.data[index]
        with open(self.path, "w") as f:
            json.dump(self.data, f)
        pass
    

