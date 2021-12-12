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
    from functools import wraps
    from time import time
    
    def time_decorating_function(func_to_test):
        prev_call_time = time()
        @wraps(func_to_test)

        def decorator(*args, **kwargs):
            if time() - prev_call_time < time_interval:
                raise RuntimeError('time_interval limit')
            prev_call_time = time()
            
            call_num = getattr(decorator, 'calls', 0)
            call_num += 1

            if call_num > n_calls:
                raise ValueError('n_calls limit')

            setattr(decorator, 'calls', call_num)
            return func_to_test(*args, **kwargs)

        setattr(decorator, 'calls', 0)

        return decorator

    return time_decorating_function
 
def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    def decorating_function(*args, **kwargs):
        try:
            return func1(*args, **kwargs)
        except:
            try:
                return func2(*args, **kwargs)
            except: 
                try:
                     return func3(*args, **kwargs)
                except:
                    try:
                        return func4(*args, **kwargs)
                    except: 
                        raise RuntimeError
        
    return decorating_function