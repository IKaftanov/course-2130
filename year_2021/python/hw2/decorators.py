
def firewall(n_calls: int, time_interval: int):


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

    from time import time
        
    def decorator(func):

        last_call_time = [time()]

        def wrapper_function(*args, **kwargs):

            if time() - last_call_time[0] < time_interval:
                raise RuntimeError(f"For the next authorized call, wait for {(time()-last_call_time[0])} seconds")

            last_call_time[0] = time()
            
            calls = getattr(wrapper_function, "n_calls", 0)
            calls += 1

            if calls == n_calls:
                raise ValueError("The maximum number of calls has been exceeded")

            setattr(wrapper_function, "n_calls", n_calls)

            return func(*args, **kwargs)

        setattr(wrapper_function, "n_calls", 0)
        return wrapper_function
    return decorator
   
@firewall(5, 10)
def foo():
    print("This is an output")
 
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