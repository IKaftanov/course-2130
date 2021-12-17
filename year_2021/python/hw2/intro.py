from typing import List, Optional, Any


def reverse(lst: Optional[List[Any]]):
   
    l = 0
    r = len(lst) - 1
    while l < r:
        tmp = lst[l]
        lst = lst[r]
        lst[r] = tmp
    return


def filter_by_indices(lst: Optional[List[Any]], indices: Optional[List[Any]]):
 
    list.sort(indices)
    num_of_del = 0
    for ind in indices:
        del lst[ind - num_of_del]
        num_of_del = num_of_del + 1
    return


# lst = [0, 1, 2, 3, 4, 5, 6, 7]
# filter_by_indices(lst, [0, 1, 7])
# print(lst)

