def fibonacci():
    i = 0
    j = 1
    k = 0
    while True:
        yield i
        k = j
        j += i
        i = k
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
