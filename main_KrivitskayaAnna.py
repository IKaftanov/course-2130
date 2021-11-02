from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __delitem__(self, value) -> bool: # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        head_val = self.head

        if head_val is not None:
            if head_val.value == value:
                # это работает, если уже первый элемент соотв.
                self.head = head_val.next_value
                head_val = None
                return True
        else:
            # это работает, если просматривался пустой лист
            return False

        bool = False
        while head_val is not None:
            # если первый эл-т не подошел, то пройтись по остальным до конца списка
            if head_val.value == value:
                bool = True
                break
            previous = head_val
            head_val = head_val.next_value
        if head_val == None:
            return bool
        previous.next_value = head_val.next_value
        head_val = None
        return bool

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        head_val = self.head

        if head_val is not None:
            if head_val.value == value:
                # это работает, если уже первый элемент соотв.
                return head_val
        else:
            # это работает, если просматривался пустой лист
            raise Exception("No elements in list at all")

        while head_val is not None:
            # если первый эл-т не подошел, то пройтись по остальным до конца списка
            if head_val.value == value:
                return head_val
            previous = head_val
            head_val = head_val.next_value
        if head_val == None:
            raise Exception("No such element in the list")
        previous.next_value = head_val.next_value
        head_val = None
        raise Exception("No such element in the list")

    def append(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next_value = Node(value)
            self.tail = self.tail.next_value

def binary_search(input_list: List[Union[int, float, str]]) -> Optional[int, float, str]:
    # судя по аргументам, тут подразумевалась сортировка,
    # а не поиск элемента
    if len(input_list) <= 1:
        return input_list
    else:
        return binary_search([e for e in input_list[1:] if e <= input_list[0]]) + [input_list[0]] +\
            binary_search([e for e in input_list[1:] if e > input_list[0]])

###################################################################################################

class BSTNode:
    def __init__(self, value=None):
        #self.parent = None
        self.left_child = None
        self.right_child = None
        self.value = value

    def _findMin(self, parent):
        """ вспомогательная для удаления: вернуть минимальный нод и его родительский """
        if self.left_child:
            return self.left_child._findMin(self)
        else:
            return [parent, self]

    def __delitem__(self, key):
        """
        вспомагательная функция для удаления элемента. Тут перепутаны key и value
        """
        if self.value == key:
            if self.right_child and self.left_child:
                [parent_min_node, min_node] = self.right_child._findMin(self)
                if parent_min_node.left_child == min_node:
                    parent_min_node.left_child = min_node.right_child
                else:
                    parent_min_node.right_child = min_node.right_child
                min_node.left_child = self.left_child
                min_node.right_child = self.right_child
                return min_node
            else:
                if self.left_child:
                    return self.left_child
                else:
                    return self.right_child
        else:
            if self.value > key:
                if self.left_child:
                    self.left_child = self.left_child.delete(key)
            else:
                if self.right_child:
                    self.right_child = self.right_child.delete(key)
        return self

class BinaryTree:
    def __init__(self):
        self.root = None

    def __getitem__(self, key) -> BSTNode:
        """
        find and return requested node
        """
        if self.root is not None:
            return self._find(key, self.root)
        else:
            return None

    # вспомогательная рекурсия для поиска
    def _find(self, key, node):
        if key == node.value:
            return node
        elif (key < node.value and node.left_child is not None):
            return self._find(key, node.left_child)
        elif (key > node.value and node.right_child is not None):
            return self._find(key, node.right_child)

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        if self.root:
            self.root = self.root.__delitem__(key)

    def append(self, bts_node: BSTNode):
        """
        add element in BTS
        """
        if self.root is None:
            self.root = bts_node
        else:
            self._add(bts_node, self.root)

    # вспомогательная рекурсия
    def _add(self, bts_node, node):
        if bts_node.value < node.value:
            if node.left_child is not None:
                self._add(bts_node, node.left_child)
            else:
                node.left_child = bts_node
        else:
            if node.right_child is not None:
                self._add(bts_node, node.right_child)
            else:
                node.right_child = bts_node


###############################################################
# пример с сортировкой листа
#list_inp = [2,5,7,3,2]
#print(binary_search(list_inp))

###############################################################
# попробовать создать нод
#trial_node = Node(5)

# попробовать пустой лист
#trial_linked_list = Linked_list()

# попробовать непустой лист
#my_list = Linked_list()
#my_list.head = Node(0)
#x2 = Node(2)
#x3 = Node(5)
#my_list.head.next_value = x2
#x2.next_value = x3
#my_list.tail = x3

# удалить элемент 1) из пустого листа, 2) 1-ый эл-т, 3) 3-ий эл-т, 4) несуществующий эл-т
#bool_del = my_list.__delitem__(6)
#print(bool_del)

# добавить эл-т в конец
#append_value = my_list.append(3)
#print(my_list.tail.value)

# get item - 1) из пустого листа, 2) вновь добавленный, 3)
#get_value = my_list.__getitem__(0)
#print(get_value)

###################################################################

# проверка добавления элементов
#tree = BinaryTree()
#tree.append(BSTNode(3))
#tree.append(BSTNode(4))
#tree.append(BSTNode(0))
#tree.append(BSTNode(8))
#tree.append(BSTNode(2))

# проверка get_item
#print(tree.__getitem__(3).value)
#print(tree.__getitem__(10))

# тут тоже все ок
#print(tree.__delitem__(3))
#print(tree.__getitem__(8).value)
