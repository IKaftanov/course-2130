from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.root = None

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if self.root is None:
            return False
        if self.root.value == value:
            self.root = self.root.next
            return True
        previous_node = self.root
        current_node = self.root.next
        while current_node != None :
            if current_node.value == value :
                previous_node.next = current_node.next
                return True
            previous_node, current_node = current_node, current_node.next
        return False
    
    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        current_node = self.root
        while current_node != None :
            if current_node.value == value :
                return current_node
            current_node = current_node.next
        return "No such value"
    
    def append(self, value):
        """
        Add element to linked list
        """
        if self.root is None:
            self.root = Node(value)
            return
        current_node = self.root
        while current_node.next != None :
            current_node = current_node.next
        current_node.next = Node(value)
        return
    
    def __repr__(self):
        node = self.root
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " - ".join(nodes)