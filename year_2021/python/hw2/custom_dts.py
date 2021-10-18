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
        self._data = []*size
        self.size = size
        self.counter = 0

    def append(self, item):
        if self.counter < self.size:
            self.data.append(item)
        else:
            self.data[self.counter%self.size] = item
        self.counter += 1
        return self.data


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
        
    def gcd(self, a, b):        
        while b:
            a, b = b, a%b
        return a        
    
    def __truediv__(self, b):
        na, da = self.nominator, self.denominator
        nb, db = b.nominator, b.denominator
        g1 = self.gcd(na, nb)
        if g1 > 1:
            na //= g1
            nb //= g1
        g2 = self.gcd(db, da)
        if g2 > 1:
            da //= g2
            db //= g2
        n, d = na * db, nb * da
        if d < 0:
            n, d = -n, -d
        return Fraction(n, d)

    def __add__(self, b):
        na, da = self.nominator, self.denominator
        nb, db = b.nominator, b.denominator
        g = self.gcd(da, db)
        if g == 1:
            return Fraction(na * db + da * nb, da * db)
        s = da // g
        t = na * (db // g) + nb * s
        g2 = self.gcd(t, g)
        if g2 == 1:
            return Fraction(t, s * db)
        return Fraction(t // g2, s * (db // g2))
        
    def __mul__(self, b):
        na, da = self.nominator, self.denominator
        nb, db = b.nominator, b.denominator
        g1 = self.gcd(na, db)
        if g1 > 1:
            na //= g1
            db //= g1
        g2 = self.gcd(nb, da)
        if g2 > 1:
            nb //= g2
            da //= g2
        return Fraction(na * nb, db * da)


    def __sub__(self, b: Fraction):
        na, da = self.nominator, self.denominator
        nb, db = b.nominator, b.denominator
        g = self.gcd(da, db)
        if g == 1:
            return Fraction(na * db - da * nb, da * db)
        s = da // g
        t = na * (db // g) - nb * s
        g2 = self.gcd(t, g)
        if g2 == 1:
            return Fraction(t, s * db, _normalize=False)
        return Fraction(t // g2, s * (db // g2))

    def __repr__(self):
        return f'{int(self.nominator/self.gcd(self.nominator, self.denominator))}/{int(self.denominator/self.gcd(self.nominator, self.denominator))}'


class MyCounter():
    """
    Реализовать тип данных `Counter`, аналогично типу из `collections`
    https://docs.python.org/3/library/collections.html#collections.Counter

    Достаточно поддерживать только два метода

    """

    def __init__(self, iterable):
        self._data = {i:iterable.count(i) for i in iterable}    

    def append(self, item):
        if item in self._data:
            self._data[item] +=1
        else: self._data[item] = 1
        return self._data

    def remove(self, item):
        self._data.pop(item, None)
        return self._data


class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = name

    def perimeter(self):
        return 2*(self.a + self.b)

    def square(self):
        return self.a*self.b

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
        pass

    def append(self, item):
        pass

    def __getitem__(self, item):
        pass

    def __delitem__(self, key):
        pass

    def __repr__(self):
        pass
