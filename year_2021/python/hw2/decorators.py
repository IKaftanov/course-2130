

def call_controller(n_calls: int, time_interval: int):
    import time
    times = 0
    time_now = time.time()
    def decorator(func):
        def decorated_func(*args, **kwargs):
            while time.time() - time_now < float(time_interval):
                while times < n_calls:
                    func(*args, **kwargs)
                    times += 1
        return decorated_func
    return decorator
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


def call_rectifier(func1, func2, func3, func4):
    functions = [func1, func2, func3, func4]
    exception_count
    for _function in functions:
        try:
            _function()
            return _function
        except:
            exception_count += 1
            continue
    if exception_count == 4:
        raise RuntimeError
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """