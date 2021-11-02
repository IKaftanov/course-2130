from __future__ import annotations

from typing import List, Any


class CycledList:
    def __init__(self, size: int):
        self._inner_idx = 0
        self._data = []
        self.size = size

    def append(self, item):
        if len(self._data) < self.size:
            self._data.append(item)
        else:
            self._inner_idx = self._inner_idx%self.size
            self._data[self._inner_idx] = item

        self._inner_idx += 1
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
        num = self.nominator*other.denominator
        dem = self.denominator*other.nominator
        return str(num // dem) + ' and ' + str(Fraction(num%dem,dem)) if num//dem != 0 else str(Fraction(num%dem,dem))
    
    def __add__(self, other):
        sum_n = self.nominator*other.denominator+other.nominator*self.denominator
        sum_d = self.denominator*other.denominator
        return str(sum_n// sum_d) + ' and ' + str(Fraction(sum_n%sum_d,sum_d)) if sum_n//sum_d != 0 else str(Fraction(sum_n%sum_d,sum_d))

    def __mul__(self, other):
        mul_n = self.nominator * other.nominator
        mul_d = self.denominator * other.denominator
        return str(mul_n//mul_d) + ' and ' + str(Fraction(mul_n%mul_d,mul_d)) if mul_n//mul_d != 0 else str(Fraction(mul_n%mul_d,mul_d))

    def __sub__(self, other):
        sub_n = self.nominator*other.denominator-other.nominator*self.denominator
        sub_d = self.denominator*other.denominator
        return str(int(sub_n/sub_d)) + ' and ' + str(Fraction(sub_n%sub_d,sub_d)) if sub_n//sub_d!= 0 else str(Fraction(sub_n%sub_d,sub_d))
    
    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'
    def __repr1__(other):
        return f'{other.nominator}/{other.denominator}'
from collections import Counter
class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter
    Достаточно поддерживать только два метода
    """

    def __init__(self, iterable):
        self._data = Counter(iterable)
        self._iterable = iterable
    def append(self, item):
        self.item=item
        self._data[self.item]+=1
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
    def __init__(self, name,side_length):
        super().__init__(name)
        self.side_length=side_length
    def perimeter(self):
        return self.side_length*4
    def square(self):
        return self.side_length*self.side_length
import json

class PersistentList:
    def __init__(self, iterable, path):
        self._iterable= iterable
        self.path = path
        with open (path,'w') as file:
            json.dump(iterable,file)      
    def append(self,item):
        self._item=item
        self._iterable.append (self._item)
        with open (self.path,'w') as file:
            json.dump(self._iterable,file)
    def delete(self, key):
        self._key=key
        self._iterable.remove (self._key)
        with open (self.path,'w') as file:
            json.dump(self._iterable,file) 
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
    def  __repr__(self):
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
    pass


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
