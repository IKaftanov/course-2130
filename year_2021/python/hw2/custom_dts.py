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
        self.i = 0 # место вставки

    def append(self, item):
        if len(self._data) == self.size:
            self._data.pop(self.i)
        self._data.insert(self.i,item)
        self.i+=1 # сдвигаем место вставки 
        self.i=self.i%self.size # проверяем, что место вставки внутри листа
    
    def print_list(self):
        # функция для отображения самого листа
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
    
    # общие функции

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self.nominator, self.denominator = Fraction.reduce(self.nominator, self.denominator)

    def __truediv__(self, other):
        na, da = self.nominator, self.denominator
        nb, db = other.nominator, other.denominator
        n, d = na * db, nb * da
        if d < 0: # знак в числитель
            n, d = -n, -d
        return Fraction(n, d) 

    def __add__(self, other):
        
        na, da = self.nominator, self.denominator
        nb, db = other.nominator, other.denominator
        
        return Fraction(na * db + da * nb, da * db)
        

    def __mul__(self, other):
        
        na, da = self.nominator, self.denominator
        nb, db = other.nominator, other.denominator
        
        return Fraction(na * nb, da * db)

    def __sub__(self, other: Fraction) -> Fraction:
        
        na, da = self.nominator, self.denominator
        nb, db = other.nominator, other.denominator
        
        return Fraction(na * db - da * nb, da * db)

    def __repr__(self):
        return f'{self.nominator}/{self.denominator}'
    
    # мои функции
    def __eq__(self, other: Fraction):
        """a == b"""
        return (self.nominator == other.nominator) and (self.denominator == other.denominator)
    
    @staticmethod
    # наибольший общий делитель
    def gcd(a, b):
        if(b==0):
            return a
        else:
            return Fraction.gcd(b,a%b)
        
    @staticmethod
    # упрощатель дробей
    def reduce(nominator, denominator):
        nod = Fraction.gcd(nominator,denominator)
        nominator /= nod
        denominator /= nod
        return int(nominator), int(denominator)


class MyCounter:
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self.iterable = iterable
        self._data = dict((x,self.iterable.count(x)) for x in set(self.iterable))

    def append(self, item):
        self.item = item
        if self.item not in self._data:
            self._data[self.item]=1
        else:
            self._data[self.item]+=1
            

    def remove(self, item):
        self.item = item
        if self.item not in self._data:
            pass
        else:
            self._data.pop(self.item)
            
    def print_counter(self):
        # функция для отображения самого счетчика
        return self._data 


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
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
        if self.a1 != self.a2:
            raise ValueError('Это не квадрат!')
    
    def perimeter(self):
        return self.a1*4

    def square(self):
        return self.a1**2


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
