import time


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

    def decorator(func):
        func.calls = 0

        def wrapper(*args, **kwargs):
            func.t = time.time()
            if func.calls < n_calls:
                func(*args, **kwargs)
                if time.time() - func.t > time_interval:
                    raise Exception('Функция превысила лимит по времени')
            else:
                raise Exception('Функция превысила лимит по вызовам')
            func.calls += 1

        return wrapper

    return decorator


def call_rectifier(*args):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    for i in args:
        try:
            i()
            return i
        except:
            continue
    raise RuntimeError
