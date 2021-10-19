def call_controller(n_calls: int, time_interval: int):#, time_interval: int):
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
    from functools import wraps
    from time import time
    
    def decorator(func):
        last = [time()]
        @wraps(func)
        def wrapper(*args, **kwargs):
            if time() - last[0] < time_interval:
                raise RuntimeError('This time not allow, please wait to {time} sec'.format(time=time()-last[0]))
            last[0] = time()
            
            calls = getattr(wrapper, 'calls', 0)
            calls += 1

            if calls == n_calls:
                raise ValueError('You have run out of posible calls')

            setattr(wrapper, 'calls', calls)
            return func(*args, **kwargs)
        setattr(wrapper, 'calls', 0)
        return wrapper
    return decorator
   
#@call_controller(5, 3)
#def f_3():
#    print(789)
 
    
def call_rectifier(lev_1, lev_2, lev_3, lev_4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    def decor(*args, **kwargs):
        try:
            return lev_1(*args, **kwargs)
        except:
            try:
                return lev_2(*args, **kwargs)
            except: 
                try:
                     return lev_3(*args, **kwargs)
                except:
                    try:
                        return lev_4(*args, **kwargs)
                    except: 
                        raise RuntimeError
        
    return decor