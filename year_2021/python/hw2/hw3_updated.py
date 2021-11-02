from __future__ import annotations

from typing import Union, List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None

    def __delitem__(self, value) -> bool:  # True -> if element was deleted else False
        """
        find item then delete
        returns True if element was deleted successfully
                False else (if element wasn't found
        """
        if self.value == value:
            if self.next_value:
                self.value = self.next_value.value
            else:
                self.value = None
            return True
        else:
            return False



    def __getitem__(self, value) -> Node:
        """
        Search for element and return
        """
        # TODO: homework

        if self.value == value:
            return self
        elif self.next_value:
            return self.next_value.__getitem__(value)
        

    def append(self, value):
        """
        Add element to linked list
        """
        # TODO: homework
        if not self.value:
            self.value = value
        else:
            self.next_value = Node(value = value)

    def __repr__(self):
        if self.value:
            return str(self.value)

class LinkedList:
    def __init__(self, input_list: List[Union[int, float, str]]):
        self.head = None
        
        for element in input_list:
            self.append(element)

    def __getitem__(self, value):
        if self.head:
            return self.head.__getitem__(value)
#         returns nothing if no head
        

    def __delitem__(self, value):
        if self.head:
            node = self.head
            value_found = False
            while node.value:
                # print("New step. The node value is", node.value)
                if value_found:
                    if node.next_value: 
                        node.value = node.next_value.value
                        # print("The new node value is", node.value)
#                         node = node.next_valu
                    else:
                        node.value = None
                value_found += node.__delitem__(value)
                # print("Is value found?", value_found, "The node_value is", node.value)
                pass
                if node.next_value:
                    node = node.next_value
                else:
                    break
            
            return self
        else:
            raise Exception("No such element in the list")

    def append(self, value):
        if not self.head:
            self.head = Node(value = value)
        else:
            node = self.head
            while node.next_value:
                node = node.next_value
            node.append(value)

            
    def __repr__(self):
        values_list = []
        node = self.head
        while node.next_value:  
            values_list.append(str(node.value))
            node = node.next_value
        if node.value:
            values_list.append(str(node.value))
        return " -> ".join(values_list)

    
if __name__ == "__main__":
    a = Node("%alia")
    llist = LinkedList(input_list=[1, 2, 3, 4])
    llist.append(5)
    print(llist.__repr__())
    llist.__delitem__(3)
    print(llist.__repr__())