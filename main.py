from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = Node(head)
        self.nodes = [self.head]

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        if value in map(lambda x: x.value, self.nodes):
            return value

        else:
            return False

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if self[value]:
            if value == self.head.value:
                self.head = self.head.next_value if self.head.next_value else Node(None)
                self.nodes = [self.head]

            else:

                if len(self.nodes) >= 3:
                    self.nodes[list(map(lambda x: x.value, self.nodes)).index(value) - 1].next_value = self.nodes[
                        list(map(lambda x: x.value, self.nodes)).index(value) + 1].value
                    del self.nodes[list(map(lambda x: x.value, self.nodes)).index(value)]

                else:
                    self.head.next_value = Node(None)
                    del self.nodes[1]

            return True

        else:
            return False

    def append(self, value):
        """
        Add element to linked list
        """
        if self.head.value is None:
            self.head = Node(value)
            self.nodes[0] = Node(value)

        else:
            self.nodes[-1].next_value = Node(value)
            self.nodes.append(Node(value))
            self.nodes[-2].next_value = self.nodes[-1]

    def __repr__(self):
        return '->'.join(map(lambda x: str(x.value), self.nodes))



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
