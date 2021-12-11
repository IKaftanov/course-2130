from __future__ import annotations

from typing import Union, List, Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None
class LL:
    def __init__(self):
        self.head = None
        
    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if self.head is None:
            return False
        else:
            x = True
            next_node = self.head
            while next_node.value != value:
                while next_node.next_value not None:
                    next_node = next_node.next_value
                x = False
                break
            next_node = next_node.next_value
            return x

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        if self.head is None:
            return self.head
        else:
            next_node = self.head
            while next_node.value != value:
                next_node = next_node.next_value
            return next_node
        

    def append(self, value):
        """
        Add element to linked list
        """
        if self.head is None:
            self.head = Node(value, None)
        else:
            next_node = self.head
            while next_node.next_value not None:
                next_node = next_node.next_value
            next_node.next_value = Node(value, None) 


def binary_search(input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:
    pass


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