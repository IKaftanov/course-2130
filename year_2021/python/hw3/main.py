from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next_value
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found)
        """
        if self.head is None:
            return False
        
        if self.head.value == value:

            if self.head.next_value:
                self.head = self.head.next_value
            else:
                self.head = None
            return True
        
        first = self.head.next_value
        second = self.head
        
        while first:
            if first.value == value:
                second.next_value = first.next_value
                return True
            second = first
            first = first.next_value
        return False
        

    def append(self, value):
        """
        Add element to linked list
        """
        if not self.head:
            self.head = Node(value)
            return
        firstnode = self.head
        while firstnode.next_value:
            firstnode = firstnode.next_value
        firstnode.next_value = Node(value)
        return
        
    
    def __getitem__(self,value):
        """
        Search for element and return
        """
        firstnode = self.head
        while firstnode == True:
            if value == firstnode.value:
                return value
            else:
                firstnode = firstnode.next_value
        return False

# tests
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(5)
ll.append(4)
ll.append (5)
print(ll)
print(ll.__delitem__(5))
print(ll)
print(ll.__getitem__(1))
    
def binary_search(input_list: List[Union[int, float, str]], value: Union[int, float, str]) -> Optional[int]:
    left = 0
    right = len(input_list)-1
    while right >= left:
        mid = (left+right) // 2
        if value == input_list[mid]:
            return mid
        else:
            if value < mid:
                right = mid-1
            else:
                left = mid+1
    return print('Object not in list')

# tests
assert binary_search([1,2,3,4,5],3) == 2
assert binary_search([1,2,3,4,5],0) == None
    
    
class BTSNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, node=None):
        self.root = node
        
        
        
    def __getitem__(self, key) -> BTSNode:
        """
        find and return requested node
        """
        if not self.root:
            return None
        
        if self.root.value == key:
            return self.root
        
        if self.root.value > key:
            return BinaryTree(self.root.left)[key]
        elif self.root.value < key:
            return BinaryTree(self.root.right)[key]
        

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        if not self.root:
            return None
        if self.root.value > key:
            self.root.left = BinaryTree(self.root.left).__delitem__(key)
        elif self.root.value < key:
            self.root.right = BinaryTree(self.root.right).__delitem__(key)
            
        else:
            
            if self.root.left is None:
                
                rfinish = self.root.right
                self.root = None
                return rfinish
            
            elif self.root.right is None:
                
                lfinish = self.root.left
                self.root = None
                return lfinish

            leaf_with_chld = self.root.right
            
            if leaf_with_chld.left is None:
                temp = leaf_with_chld.left

            self.root.value = leaf_with_chld.value
            
            self.root.right = BinaryTree(self.root.right).__delitem__(leaf_with_chld.value)
            
        return self.root
            
            

    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """  
        if not self.root:
            self.root = bts_node
        else:
            if self.root.value < bts_node.value:
                self.root.right = BinaryTree(self.root.right).append(bts_node)
            elif self.root.value > bts_node.value:
                self.root.left = BinaryTree(self.root.left).append(bts_node)
        return self.root

#tests
tree=BinaryTree()
tree.append(BTSNode(4))
tree.append(BTSNode(5))
tree.append(BTSNode(3))
tree.append(BTSNode(7))
tree.__delitem__(3)
