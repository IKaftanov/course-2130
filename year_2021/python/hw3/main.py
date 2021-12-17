from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value=None

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        # TODO: homework
        cur = self .next_value
        pre=None
        while cur!=None:
            if cur.value==value:
                if cur==self.next_value:
                    self.next_value=cur.next_value
                else:
                    pre.next_value=cur.next_value
                return True
        pass
        return False

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        # TODO: homework
        cur = self.next_value
        while not cur:
            if cur.value==value:
                return cur
            else:
                cur = cur.next_value
        return None
        pass



    def append(self, value):
        """
        Add element to linked list
        """
        node = Node(value)
        if self.next_value == None:
            self.next_value=node

        cur=self.next_value

        while cur.next_value != None:
            cur = cur.next_value
        cur.next_value = node

        # TODO: homework
        pass


def binary_search(input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:
    
    pass


class BTSNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        pass


class BinaryTree:
    def __init__(self):
        self.root=None
        pass

    def __getitem__(self, key) -> BTSNode:
        """
        find and return requested node
        """
        if self.root:
            return self._get(key,self.root)

        pass
    def _get(self,val,node):
        if not node:
            return None
        elif node.value == val:
            return node
        elif val < node.value:
            return self._get(val, node.left)
        else:
            return self._get(val, node.right)

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        nodeToDelete = self.__getitem__(key)
        if nodeToDelete:
            self._delitem(nodeToDelete)
        else:
            raise KeyError('Error, key not in tree')

    def _delitem(self,node):
        if not node.left and node.right:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.right and node.left:
            minNone = self._findMin(node.right)
            node.value = minNone.value
            self._delitem(minNone)
        else:
            if node.left:
                if node.parent and node.parent.left == node:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.parent and node.parent.right == node:
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    self.root = node.left
                    node.left.parent = None
                    node.left = None
            else:
                if node.parent and node.parent.left == node:
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.parent and node.parent.right == node:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    self.root = node.right
                    node.right.parent = None
                    node.right = None

    def _findMin(self, node):
        if node:
            currentNode = node
            while currentNode.left:
                currentNode = currentNode.left
            return currentNode
    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        if not self.root:
            self.root=bts_node
        else:
            cur=self.root
            while True:
                if bts_node.val < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = bts_node
                        bts_node.parent = cur
                        break
                elif bts_node.val > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = bts_node
                        bts_node.parent = cur
                        break
                else:
                    break
