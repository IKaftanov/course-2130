
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
    fib1, fib2 = 0, 1
    while True:
        yield fib1
    fib1, fib2 = fib2, fib1 + fib2