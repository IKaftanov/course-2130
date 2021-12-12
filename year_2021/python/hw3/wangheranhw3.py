from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.cur = None
        self.count = 0

    def getList(self):
        temp =self.head
        while temp != None:
            yield temp.value
            temp = temp.ref

    def __delitem__(self, value) -> bool:
        temp =self.head
        while temp != None:
            if temp.value == value and temp == self.head:
                self.head = temp.ref
                del temp
                self.count -= 1
                return
            elif temp.ref != None and temp.ref.value == value:
                temp_ref = temp.ref.ref
                del temp.ref
                self.count -= 1
                temp.ref = temp_ref
                return
            temp = temp.ref


    def __getitem__(self, value) -> Node:
        i = 0
        temp = self.head

        if type(value) is int:
            while temp != None:
                if i == value:
                    return temp.value
                temp = temp.value
                i += 1
            return


    def append(self, value):
        if self.head is None:
            self.cur = Node(value)
            self.head = self.cur
        else:
            self.cur.ref = Node(value)
            self.cur = self.cur.ref
        self.count += 1


def binary_search(input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:
    pass


class BTSNode:
    def __init__(self):
        BTSNode0 = BTSNode()
        BTSNode1 = BTSNode(height= 2, is_perfect = True)
        BTSNode2 = BTSNode(height= 2, is_perfect = Flase)

class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, key):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.left is None:
                temp_node.left = node
                return
            else:
                queue.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = node
                return
            else:
                queue.append(temp_node.right)

            def bre_search(self, key):
                if self.root.key == key:
                    return self.root
                queue = [self.root]
                while queue:
                    temp_node = queue.pop(0)
                    if temp_node.left and temp_node.left.key == key:
                        return temp_node.left
                    if temp_node.right and temp_node.right.key == key:
                        return temp_node.right
                    if temp_node.left:
                        queue.append(temp_node.left)
                    if temp_node.right:
                        queue.append(temp_node.right)
                return None

    def __getitem__(self, key) -> BTSNode:
        if self.root.key == key:
            return None
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.left and temp_node.left.key == key:
                return temp_node
            if temp_node.right and temp_node.right.key == key:
                return temp_node
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        return None

    def __delitem__(self, key):
        if Node is None:
            return
        if Node.key == key and Node == self.root:
            self.root = None
            return
        if Node.key == key:
            Node.left = None
            Node.right = None
            return node.value
        left_part = self.del_key(Node.left, key)
        if left_part:
        	self.flag = True
            Node.left = None
        right_part = self.del_value(Node.right, key)
        if right_part:
        	self.flag = True
            Node.right = None
        return None



    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        pass