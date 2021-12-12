def test_reverse():
    assert reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse([]) == []


def test_filter_by_indices():
    assert filter_by_indices([1, 2, 3, 4], [0, 1]) == [3, 4]
    assert filter_by_indices([1, 2], [0, 1, 2]) == []
    assert filter_by_indices([1, 2], []) == [1, 2]
    assert filter_by_indices([], [0, 1]) == []


def test_legacy_t1():
    assert legacy.t1(3) == 20
    assert legacy.t1(-5) == 0
    assert legacy.t1(19) == 20
    assert legacy.t1(20) == 20


def test_legacy_t2():
    assert legacy.t2('abc abc abc') == 'cba cba cba'
    assert legacy.t2('') == ''


def test_legacy_t3():
    assert legacy.t3({'a': 1, 'b': 2}) == 'a: 1; b: 2'
    assert legacy.t3({}) == ''


def test_legacy_t4():
    assert legacy.t4('abcd', 'cb')=='Есть'
    assert legacy.t4('', '')=='Есть'
    assert not legacy.t4('ab', 'cx')=='Нет'

def test_legacy_t5():
    assert legacy.t5(['abd',5,7,'avc',5])==[5, 7, 5, 175]
    
def test_fibonacci():
    iterator = fibonacci()
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5


def test_cycled_list():
    cycled_list = custom_dts.CycledList(3)
    cycled_list.append(1)
    cycled_list.append(2)
    cycled_list.append(3)
    cycled_list.append(4)
    assert cycled_list._data == [4, 2, 3]


def test_call_rectifier():
    def f1():
        return 1

    def f1_2():
        raise Exception

    def f2():
        return 2

    def f3():
        return 1

    def f4():
        return 1

    wrapper = call_rectifier(f1, f2, f3, f4)
    assert wrapper() == 1
    wrapper = call_rectifier(f1_2, f2, f3, f4)
    assert wrapper() == 2


def test_fraction():
    fract = custom_dts.Fraction(5,4)
    other = custom_dts.Fraction(30,2)
    assert (Fraction(5,4)+Fraction(30,2))==fract.__add__(other)
    assert (Fraction(5,4)-Fraction(30,2))==fract.__sub__(other)
    assert (Fraction(5,4)/Fraction(30,2))==fract.__truediv__(other)
    assert (Fraction(5,4)*Fraction(30,2))==fract.__mul__(other)

def test_counter():
    counter = custom_dts.MyCounter([1, 1, 2, 3])
    assert counter._data == {1: 2, 2: 1, 3: 1}
    counter.append(1)
    assert counter._data == {1: 3, 2: 1, 3: 1}
    counter.remove(2)
    assert counter._data == {1: 3, 3: 1}
    counter.remove(1)
    assert counter._data == {3: 1}


def test_square():
    square = custom_dts.Square(10, 10)
    assert square.perimeter() == 40
    assert square.square() == 100


def test_persistent_list():
    def read_store(file_path):
        with open(file_path) as file:
            json.load(file)

    store_path = 'store'

    persistence_list = custom_dts.PersistentList([1, 2, 3], store_path)
    assert read_store(store_path) == [1, 2, 3]
    persistence_list.append([1, 2, 3])
    assert read_store(store_path) == [1, 2, 3, [1, 2, 3]]
    persistence_list.delete(-1)
    assert read_store(store_path) == [1, 2, 3]
    persistence_list.delete(4)
    assert read_store(store_path) == [1, 3]
    assert persistence_list[0] == 1
