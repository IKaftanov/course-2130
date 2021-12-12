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
    a = str (lst [::-1])
    print (a)   
def filter_by_indices(lst, indices):
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
    return [val for i, val in enumerate(lst) if i not in indices] 
