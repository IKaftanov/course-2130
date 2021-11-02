from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

    def append(self, value):
        """
        Add element to linked list
        """

        last = Node(value)
        pointer = self
        while (pointer.next_value):
            pointer = pointer.next_value
        pointer.next_value = last
        pass
    
class LinkedList:
    def init(self):
        self.head = None
    
    def __delitem__(self, value):
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        target_value = value
        if self.head is None:
            return False

        if self.head.value == target_value:
            self.head = self.head.next_value
            return True

        previous_node = self.head
        for node in self:
            if node.value == target_value:
                previous_node.next_value = node.next_value
                return True
            previous_node = node

        return False
    def __getitem__ (self, value):
        """
        Search for element and return
        """
        
        # define current_node
        current_node = self.head
        
        # define position
        node_id = 1
        
        # define list of results
        results = []
        
        while current_node is not None:
            if current_node.value = value:
                results.append(node_id)
                
            # jump to the linked node
            current_node = current_node.next_value
            node_id = node_id + 1
        
        return results


def binary_search(input_list: List[Union[int, float, str]],value) -> Optional[int, float, str]:
    left, right = 0, len(input_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if input_list[middle] == value:
            return middle

        if input_list[middle] < value:
            left = middle + 1
        elif input_list[middle] > value:
            right = middle - 1
    pass


class BTSNode:
    def __init__(self, value, parent_node = None):
        self.left  = None
        self.right = None
        self.value = value
        if parent_node == None:
            self.parent = self
        else:
            self.parent = parent_node
        pass
    
class BinaryTree:
    def __init__(self):
        self.root = None
        pass

    
    def __getitem__(self, key):
        """
        find and return requested node
        """
        if self.root is not None:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, node):
        if key == node.value:
            return node
        elif (key < node.value and node.left is not None):
            return self._find(key, node.left)
        elif (key > node.value and node.right is not None):
            return self._find(key, node.right)

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        pass
    def delete(self, key):
    """ delete the node with the given key and return the 
    root node of the tree """

        if self.value == key:
            
            if self.right and self.left: 
                [psucc, succ] = self.right._findMin(self)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                succ.left = self.left
                succ.right = self.right
                return succ                

            else:
                if self.left:
                    return self.left 
                else:
                    return self.right 
        else:
            if self.value > key:  
                if self.left:
                    self.left = self.left.delete(key)
            else:                      
                if self.right:
                    self.right = self.right.delete(key)
        return self

    def _findMin(self, parent):
    """ return the minimum node in the current tree and its parent """

        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]
    def append(self, bts_node: BTSNode):
        if self.root is None:
            self.root = BTSNode(bts_node)
        else:
            self._add(bts_node, self.root)

    def _add(self, bts_node, node):
        if bts_node < node.value:
            if node.left is not None:
                self._add(bts_node, node.left)
            else:
                node.left = Node(bts_node)
        else:
            if node.right is not None:
                self._add(bts_node, node.right)
            else:
                node.right = BTSNode(bts_node)
