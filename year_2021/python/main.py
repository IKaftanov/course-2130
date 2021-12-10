from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if not self.head:
            return False
        if self.head.value == value:
            if self.head.next_value:
                self.head = self.head.next_value
            else:
                self.head = None
            return True
        link = self.head.next_value
        prev = self.head
        while link:
            if link.value == value:
                prev.next_value = link.next_value
                return True
            prev = link
            link = link.next_value
        return False

    pass

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        self.value = value
        self.next_value = None
        if value in map(lambda x: x.value, self.nodes):
            return value

        else:
            return False



    def append(self, value):
        """
        Add element to linked list
        """
        if not self.head:
            self.head = Node(value)
            return
        link = self.head
        while link.next_value:
            link = link.next_value
        link.next_value = Node(value)
        return



def binary_search(value, input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:

    left = 0
    right = len(input_list) - 1
    while left <= right:
        m = (left + right) // 2
        if input_list[m] == value:
            return m
        elif input_list[m] < value:
            left = m + 1
        else:
            right = m - 1
    return None


class BTSNode:
    def __init__(self):
        pass


class BinaryTree:
    def __init__(self):
        pass

    def __getitem__(self, key) -> BTSNode:
        """
        find and return requested node
        """
        pass

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        pass

    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        pass