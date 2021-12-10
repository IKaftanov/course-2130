import time

def call_controller(foo, n_calls: int, time_interval: int):
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
start = time.time()
for i in range(n_calls) :
    if time.time() - start >= time_interval:
        break
        foo()

def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    i = 0
    for i in [func1, func2, func3, func4] :
        i += 1
        try :
            f()
            break
        expect :
            if i==4 :
                raise Exception('RuntimeError')
            pass    
    pass
