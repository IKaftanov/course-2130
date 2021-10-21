

def call_controller(n_calls: int, time_interval: int):
    """
    Напишите функцию декоратор, которая ограничивает количество вызовов функции.

    ```
    n_calls: количество возможнх вызовов
    time_interval: время в секундах
    ```

    ```
    @firewall(10, 20):
    def foo():
      pass
    ```
    """
    def OurDecorator(func):
        def wrapper():
            wrapper.count += 1
            if wrapper.count <= n_calls:
                func()
        wrapper.count = 0
        return wrapper
    return OurDecorator

def f1():
    print('Ilya 24')


def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    def wrapper():
        try:
            return func1()
        except:
            try:
                return func2()
            except:
                try:
                    return func3()
                except:
                    try:
                        return func4()
                    except:
                        raise RuntimeError
    return wrapper

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