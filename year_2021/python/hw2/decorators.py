
import time
def call_controller(n_calls: int, time_interval: int):
    count = [0]

    def decorator(fn):
        def function(*args, **kwargs):
            time.sleep(time_interval)
            if count[0] < n_calls:
                count[0] += 1
                return fn(*args, **kwargs)
            else:
                return

        return function

    return decorator

def call_rectifier(func1, func2, func3, func4):

    functions = { func1, func2, func3, func4}
    for i in functions :
        try :
            i()
            return i
        except:
            continue
        raise RuntimeError