

def call_controller(n_calls: int, time_interval: int):
    """
    Напишите функцию декоратор, которая ограничивает количество вызовов функции.

    ```
    n_calls: количество возможнх вызовов
    time_interval: время в секундах
    ```
    """
    def foo():
        pass
        
    for i in range(n_calls):
        foo()
        time.sleep(time_interval)

def call_rectifier(func1, func2, func3, func4):
    """
    Напишите декоратор который на вход принимает 4 функции и следует следующие логике:
        1. Запускает функцию, если она завершается с ошибкой, то запускает следующую
        2. Если все функции завершились ошибкой (exception) -> вызвает exception `RuntimeError`
    """
    def runtimer():
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
                        raise RuntimeError('Время вышло')
    return runtimer
        