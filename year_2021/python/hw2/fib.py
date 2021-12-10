
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
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c
