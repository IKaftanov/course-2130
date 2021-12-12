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

            self.n = n


        def __iter__(self):  

            self.x1 = 0
            self.x2 = 1
            return self

        def __next__(self):

            N = self.x1                 
            self.x1, self.x2 = self.x2, self.x1 + self.x2
            return N
    
    return iter(Fibonacci(0))
