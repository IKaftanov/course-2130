
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
    pass
  pass
    num = [0,1,1]
    while True:
        yield num[0]
        del(num[0])
        num.append(num[0] + num[1])
