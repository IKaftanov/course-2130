class Fibonacci:                                        
    def __init__(self):                      
        self.n = 0

    def __iter__(self):                           
        self.last_num = 0
        self.next_num = 1
        return self

    def __next__(self):   
        if self.n == 0:
            self.n += 1
            return self.last_num
        else:
            self.n += 1
            self.last_num, self.next_num = self.next_num, self.last_num + self.next_num
            return self.last_num
        
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
    
    return iter(Fibonacci())