
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
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b