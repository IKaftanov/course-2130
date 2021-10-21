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
    reverse_list = lst[::-1]
    return reverse_list



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
    for i in range(len(indices)):
        a = indices[i]
        if a < 0:
            a = a + len(lst)
    indices.sort()
    j = 0
    for j in range(len(indices)):
        a = indices[j]
        if a >= x:
            continue
        c = a - j
        j = j + 1
        del lst[c]
    return lst
