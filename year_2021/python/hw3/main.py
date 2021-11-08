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
        return ' -> '.join(nodes)

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found)
        """
        if self.__getitem__(value) is not None:
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    if previous is None:
                        self.head = current.next_value
                    else:
                        previous.next_value = current.next_value
                previous = current
                current = current.next_value
            return True
        else:
            return False

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            else:
                node = node.next_value

    def append(self, value):
        """
        Add element to linked list
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_value:
                current = current.next_value
            current.next_value = new_node


# Создание связанного списка
l = LinkedList()

# Проверка операции добавления элемента в список
l.append(1)
l.append(2)
l.append(3)
print(l)

# Проверка операции получения элемента из списка
print(l[2])
print(l[4])

# Проверка операции удаления
print(l.__delitem__(2))
print(l.__delitem__(4))
print(l)


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
