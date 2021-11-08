from __future__ import annotations

from typing import Union, List, Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete

        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        # TODO: homework

        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == value:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == value:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % value)


    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        curr = self.head
        while curr and curr.data != value:
            curr = curr.next
        return curr

    def append(self, value):
        """
        Add element to linked list
        """
        if self.head is None:
            self.head = value
            return
        for current_node in self:
            pass
        current_node.next = value


def binary_search(input_list: List[Union[int, float, str]], x) -> Optional[int, float, str]:
    low = 0 
    high = len(input_list) - 1 
    mid = 0
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1

class BTSNode:
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree():
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def append(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.append(val)
                return
            self.left = BinaryTree(val)
            return

        if self.right:
            self.right.append(val)
            return
        self.right = BinaryTree(val)

    def __delitem__(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.__delitem__(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.__delitem__(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.__delitem__(min_larger_node.val)
        return self

    def __getitem__(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.__getitem__(val)

        if self.right == None:
            return False
        return self.right.__getitem__(val)
