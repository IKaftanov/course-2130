from typing import List, Optional, Any


def reverse(lst: Optional[List[Any]]):
    x = lst[::-1]
    """
    Напишите функцию, котороя разворачивает список, используя срезы (индексацию элементов).
    Input:
    ```
        [1, 2, 3, 4]
    ```
    Oputput:
    ```
        [4, 3, 2, 1]
    ```
    """
    return x


def filter_by_indices(lst: Optional[List[Any]], indices: Optional[List[Any]]):
    x = lst
    for i in sorted(indices, reverse = True):
        if i < len(x):
            del x[i]
    """
    Напишите функцию, которая удаляет список индексов из списка.
    (
      Для удаления используется оператор `del`: `del my_list[1]` или `.pop()`
    )
    Input:
    ```
        [1, 2, 3, 4], [0, 1]
    ```
    Output:
    ```
        [3, 4]
    ```
    """
    return x