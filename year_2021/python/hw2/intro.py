from typing import List, Optional, Any


def reverse(lst: Optional[List[Any]]):
    """
    Напишите функцию, которая разворачивает список, используя срезы (индексацию элементов).

    Input:
    ```
        [1, 2, 3, 4]
    ```

    Output:
    ```
        [4, 3, 2, 1]
    ```
    """
    new_lst = lst[::-1]
    return new_lst


def filter_by_indices(lst: Optional[List[Any]], indices: Optional[List[Any]]):
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
    indices.sort()
    if lst:
        for i in indices[::-1]:
            if i in range(len(lst)):
                del lst[i]
    return lst

