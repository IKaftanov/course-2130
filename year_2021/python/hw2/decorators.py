
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
    
    
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            a = 0
            time0 = time()
            calls = 0
            while a==0:
                
                #Проверяем, что временной промежуток ещё не закончился
                if time() - time0 < time_interval:
                    #проверяем, что на данный момент лимит по вызову функций ещё не был исчерпан
                    if calls < n_calls:
                        calls +=1
                        return func(*args, **kwargs)
                    else:
                        a = 1
                        time.sleep(time=time_interval - time() + time0)
                        
                else:
                    a=1
                    #Если мы перешли на новый временной промежуток, то вызываем функцию
                    return func(*args, **kwargs)
            
        return wrapper
    return decorator
   

    
   






def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """

    def my_function(*args, **kwargs):
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
        
    return my_function
    



