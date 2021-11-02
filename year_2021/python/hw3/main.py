from __future__ import annotations


class LinkedList:

    head = None

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
        if self.head == None:
           raise Exception('There is nothing to delete')

        if self.head == value:
            self.head = self.head.next_value
            return True

        search = self.head
        while search.value != None:
            if search.value == value:
                search.value = search.next_value
                return True
            search = search.next_value
        else: return False

    def __getitem__(self, value):
        """
        Search for element and return
        """
        if self.head == value:
            return self.head
        search = self.head
        while search.value != None:
            if search.value == value:
                return search.value
            search = search.next_value
        return False

    def append(self, value):
        """
        Add element to linked list
        """
        if self.head == None:
            self.head = self.Node(value)

        lastnode = self.head
        while lastnode.next_value != None:
            lastnode = lastnode.next_value
        lastnode.next_value = self.Node(value)


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
assert l1.__getitem__(3) == 3
assert l1.__delitem__(4) == True




def binary_search(input_list, x) :
    n = len(input_list)
    if n > 1:
        if input_list[int(n/2)] == x:
            return x
        elif input_list[int(n/2)] > x:
            return binary_search(input_list[:int(n/2)], x)
        else: return binary_search(input_list[int(n/2):], x)
    else: return x

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
x = 5
assert binary_search(arr, x) == 5

class BinaryTree:
    class BTSNode:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    root: BTSNode = None

    def __getitem__(self, key):
        """
        find and return requested node
        """
        search = self.root
        if self.root == key or self.root == None:
            return print('Дерево пустое')
        while search != None:
            if search.value < key:
                if search.right_child:
                    search = search.right_child
                else: return print('Not found')
            elif search.value > key:
                if search.left_child:
                    search = search.left_child
                else: return print('Not found')
            elif search.value == key:
                return print(search.value)
            else: return print('Not found')

    def __delitem__(self, key):
        """
        find and delete item from tree by key
        be careful with different cases on delete
        """
        if self.root == None:
            return False

        search = self.root
        while search != None:
            if search.value < key:
                search = search.right_child
            elif search.value > key:
                search = search.left_child
            elif search.value == key:
                if search.left_child == None and search.right_child == None:
                    search.value = None
                    return print(True)
                elif search.left_child == None and search.right_child != None:
                    search.value = search.right_child
                    search.right_child = None
                    return print(True)
                elif search.left_child != None and search.right_child == None:
                    search.value = search.left_child
                    search.left_child = None
                    return print(True)
                else:
                    min_r = search.right_child
                    while min_r.left_child != None:
                        min_r = min_r.left_child
                    search.value = min_r.value
                    min_r = None
                    return print(True)
        else: return False

    def append(self, key):
        """
        add element in BTS
        """
        if self.root == None:
            self.root = self.BTSNode(key)
            return self.BTSNode(key)

        search = self.root
        while search.value != None:
            if search.value == key:
                return 'Already exists'
            elif search.value < key and search.right_child != None:
                search = search.right_child
            elif search.value < key and search.right_child == None:
                search.right_child = self.BTSNode(key)
                return True
            elif search.value > key and search.left_child != None:
                search = search.left_child
            elif search.value > key and search.left_child == None:
                search.left_child = self.BTSNode(key)
                return True


bin = BinaryTree()
bin.append(4)
bin.append(2)
bin.append(10)
bin.append(40)
bin.append(50)
bin.append(33)
bin.__getitem__(10)
bin.__getitem__(11)
bin.__delitem__(40)
bin.__delitem__(20) == False