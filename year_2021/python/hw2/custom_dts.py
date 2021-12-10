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
	@@ -47,18 +61,31 @@ class Fraction:
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
	@@ -74,18 +101,26 @@ class MyCounter:
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
	@@ -101,7 +136,18 @@ class Square(Figure):
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
