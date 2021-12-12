
def fibonacci(a1=0, a2=1):
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
    while True:
        yield a1
        a2, a1 = a1 + a2, a2
