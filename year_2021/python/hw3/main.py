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


def binary_search(input_list: List[Union[int, float, str]], element) -> Optional[int, float, str]:
    sorted_list = sorted(input_list)
    middle_element = sorted_list[len(sorted_list) // 2]

    if middle_element == element:
        return element

    elif len(input_list) > 1:
        left_list = sorted_list[:len(sorted_list) // 2]
        right_list = sorted_list[int(len(sorted_list) / 2) + 1:]

        return binary_search(left_list, element) if element < middle_element else binary_search(right_list, element)

    else:
        return False


class BTSNode:
    def __init__(self, key, left_child=None, right_child=None):
        """
        key - ключ узла
        left_child - левый потомок (BTSNode)
        right_child - правый потомок (BTSNode)
        """
        self.key = key
        self.left_child = left_child
        self.right_child = right_child

    def __add__(self, other):
        if other.key < self.key and not self.left_child:
            self.left_child = other
        elif other.key > self.key and not self.right_child:
            self.right_child = other
        else:
            raise Exception('Все потомки заняты')

    def __repr__(self):  # чтобы красиво выводилось
        if self.left_child is not None and self.right_child is not None:
            return (' ' * len(str(self.left_child.key)) + str(self.key) + '\n' +
                    ' ' * int(len(str(self.left_child.key)) / 2) + '/' + ' ' * len(str(self.key)) + ' \\' + '\n' +
                    str(self.left_child.key) + ' ' * len(str(self.key)) + str(self.right_child.key))
        elif self.left_child is not None:
            return (' ' * len(str(self.left_child.key)) + str(self.key) + '\n' +
                    ' ' * int(len(str(self.left_child.key)) / 2) + '/' + '\n' +
                    str(self.left_child.key))
        elif self.right_child is not None:
            return (str(self.key) + '\n' +
                    ' ' * len(str(self.key)) + ' \\' + '\n' +
                    ' ' * len(str(self.key)) + str(self.right_child.key))
        else:
            return str(self.key)


class BinaryTree:
    def __init__(self, root: BTSNode):
        self.root = root

    def __getitem__(self, key) -> BTSNode:
        """
        find and return requested node
        """
        try:
            if key == self.root.key:
                return self.root
            elif key < self.root.key:
                return BinaryTree(self.root.left_child).__getitem__(key)
            else:
                return BinaryTree(self.root.right_child).__getitem__(key)
        except:
            raise Exception('Элемент с таким ключом не существует')

    def find_successor(self, key):
        node = self[key].right_child
        successor_value = node.key
        while node.left_child:
            successor_value = node.left_child.key
            node = node.left_child
        del self[successor_value]
        return successor_value

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        if self[key]:
            node = self.root
            prev_node = None
            while node.left_child or node.right_child:
                if node.left_child and key < node.key:
                    node, prev_node = node.left_child, node
                elif node.right_child and key > node.key:
                    node, prev_node = node.right_child, node
                else:
                    break

            if not (node.left_child or node.right_child):  # первый случай - удаляю вершину без потомков
                if not prev_node:  # если надо удалить корень
                    node.key = None
                else:
                    if key < prev_node.key:
                        prev_node.left_child = None
                    else:
                        prev_node.right_child = None

            elif node.left_child and not node.right_child:  # второй случай - удаляю вершину с 1 потомком
                if not prev_node:  # если надо удалить корень
                    node.key, node.left_child, node.right_child = node.left_child.key, node.left_child.left_child, node.left_child.right_child
                else:
                    if key < prev_node.key:
                        prev_node.left_child, node.right_child, node.left_child = node.left_child, node.left_child.right_child, node.left_child.left_child
                    else:
                        prev_node.right_child, node.right_child, node.left_child = node.left_child, node.left_child.right_child, node.left_child.left_child

            elif not node.left_child and node.right_child:
                if not prev_node:  # если надо удалить корень
                    node.key, node.left_child, node.right_child = node.right_child.key, node.right_child.left_child, node.right_child.right_child
                else:
                    if key < prev_node.key:
                        prev_node.left_child, node.right_child, node.left_child = node.right_child, node.right_child.right_child, node.right_child.left_child,
                    else:
                        prev_node.right_child, node.right_child, node.left_child = node.right_child, node.right_child.right_child, node.right_child.left_child

            else:  # есть оба потомка
                node.key = BinaryTree(node).find_successor(key)

        else:
            raise Exception('Элемент с таком ключом не существует')

    def append(self, bts_node: BTSNode):
        """
        add element in BTS
        """
        if not self.root.key:
            self.root = bts_node
        else:
            node = self.root
            while node.left_child or node.right_child:
                if node.left_child and bts_node.key < node.key:
                    node = node.left_child
                elif node.right_child and bts_node.key > node.key:
                    node = node.right_child
                else:
                    break
            node + bts_node
            pass

    def __repr__(self):
        return str(self.root)
