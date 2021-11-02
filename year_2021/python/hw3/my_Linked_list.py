from __future__ import annotations

#from typing import Union, List, Optional


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
        head_value = self.head

        # Проверка, не пустой ли лист
        if head_value is None:
            return False
        else:
            # Случай соответствия первому элементу
            if head_value.value == value:
                self.head = head_value.next_value
                head_value = None
                return True


        check = False
        #  Проход по листу в поиске нужного элемента
        while head_value is not None:
            if head_value.value == value:
                check = True
                break
            previous_value = head_value
            head_value = head_value.next_value
        if head_value == None:
            return check
        previous_value.next_value = head_value.next_value
        head_value = None
        return check

    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        head_value = self.head

        # Проверка на пустой лист
        if head_value is None:
            raise Exception("Такого элемента в листе нет")
        else:
            # Случай соответствия первому элементу
            if head_value.value == value:
                return head_value
            
            
        #  Проход по листу в поиске нужного элемента
        while head_value is not None:
            if head_value.value == value:
                return head_value
            previous_value = head_value
            head_value = head_value.next_value
        if head_value == None:
            raise Exception("Такого элемента в листе нет")
        previous_value.next_value = head_value.next_value
        head_value = None
        raise Exception("Такого элемента в листе нет")

    def append(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next_value = Node(value)
            self.tail = self.tail.next_value




