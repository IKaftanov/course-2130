from typing import List, Optional, Any


def reverse(lst: Optional[List[Any]]):
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
    rev_lst = lst[::-1]
    return rev_lst


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
    x = len(lst)
    i = 0
    while i != len(indices):
        if abs(indices[i]) >= x:
            del indices[i]
            i -= 1
        if indices[i] < 0:
            indices[i] += x
        i += 1
    
    indices.sort()
    x = len(lst)
    
    k = 0
    for i in set(indices):
        if(abs(i) >= x):
            continue
        del(lst[i - k])
        k += 1
    return lst
