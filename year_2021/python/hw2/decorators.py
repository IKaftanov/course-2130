

def call_controller(n_calls: int, time_interval: int):
    """
    Напишите функцию декоратор, которая ограничивает количество вызовов функции.

    ```
    n_calls: количество возможных вызовов
    time_interval: время в секундах
    ```

    ```
    @firewall(10, 20):
    def foo():
      pass
    ```
    """
    def wrapper(f):
        f.max = n_calls
        f.called = 0

        def surrogate(*args, **kwargs):
            f.called += 1
            if f.called <= f.max:
                return f(*args, **kwargs)
            else:
                raise RuntimeError("Достигнут лимит по вызовам.")

        return surrogate

    return wrapper


def call_rectifier(func1, func2, func3, func4):
    """
        Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
            1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
            2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    def wrapper():
        for func in func1, func2, func3, func4:
            try:
                return func()
            except Exception:
                if func == func4:
                    raise RuntimeError
                else:
                    continue
    return wrapper
