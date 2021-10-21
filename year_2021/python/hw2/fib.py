def fibonacci():
    """
    # Задание 4
    Написать генератор чисел Фибоначчи
    Input:
    ```
    ```
    Output:
    ```
        next call: 0
        next call: 1
        ...
    ```
    """
    class Fibonacci:                                        
        def __init__(self, n):                      
            pass

        def __iter__(self):                           
            self.a = 0
            self.b = 1
            return self

        def __next__(self):                           
            fib = self.a                 
            self.a, self.b = self.b, self.a + self.b
            return fib
    
    return iter(Fibonacci(0))
