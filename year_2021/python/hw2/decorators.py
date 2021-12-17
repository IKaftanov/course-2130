
import time

def call_controller(n_calls: int, time_interval: int):
   


    def decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            for i in range(n_calls - 1):
                func(*args, **kwargs)
                time.sleep(time_interval)

        return wrapper

    return decorator

def call_rectifier(func1, func2, func3, func4):
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except RuntimeError:
                try:
                    func1(*args, **kwargs)
                except RuntimeError:
                    try:
                        func2(*args, **kwargs)
                    except RuntimeError:
                        try:
                            func3(*args, **kwargs)
                        except RuntimeError:
                            try:
                                func4(*args, **kwargs)
                            except RuntimeError:
                                raise RuntimeError

        return wrapper

    return decorator


@call_controller(10, 2)
def say_hello():
    print('привет')

say_hello()



