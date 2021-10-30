from __future__ import annotations

from typing import Union, List, Optional


class LinkedList:
    head=None
    class Node:
        def __init__(self, value):
            self.value = value
            self.next_value = None
            
    def append(self, value):
        """
        Add element to linked list
        """
        if not self.head:
            self.head=self.Node(value)
            return value
        node=self.head
        while node.next_value:
            node=node.next_value
        node.next_value=self.Node(value)
    
    def out(self):
        node=self.head
        while node.next_value:
            print(node.value)
            node=node.next_value
        print (node.value)
        
    def __getitem__(self,value):
        lastnode = self.head
        while (lastnode):
            if value == lastnode.value:
                return value
            else:
                lastnode = lastnode.next_value
        return False
    
    def __delitem__(self, dlvalue):
        headvalue = self.head
        #проверяем есть ли в первом узле удаляемое значение
        if headvalue is not None:
            if headvalue.value==dlvalue:
                return True
                self.head = headvalue.next_value
                headvalue = None
                return
        #проверяем дальше
        while headvalue is not None:
            if headvalue.value==dlvalue:
                return True
                break
            lastvalue = headvalue
            headvalue = headvalue.next_value
            
        if headvalue == None:
            return False
        lastvalue.next_value = headvalue.next_value 
        headvalue = None
#проверка
ll=LinkedList()
ll.append(1)
ll.append (2)
ll.append(3)
ll.append(4)
ll.append (5)
ll.__delitem__(5)


def binary_search(input_list,x,start,stop):
    if start>stop:
        return False
    else: 
        mid=(start+stop)//2
        if x==input_list[mid]:
            return mid
        elif x<input_list[mid]:
            return binary_search(input_list,x,start,mid-1)
        else:
            return binary_search(input_list,x,mid+1,stop)

input_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x=10
start=0
stop=len(input_list)
i=binary_search(input_list,x,start,stop)
if i==False:
    print('элемент не найден')
else:
    print ('Элемент найден')

class BTSNode:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None
class BinaryTree:
    def __init__(self):
        self.root=None
        self.size=0
    def __getitem__(self, value) -> BTSNode:
        """
        find and return requested node
        """
        if self.root:
            is_found = self._getitem(value,self.root)
            if is_found:
                return True
            return False 
        else:
            return None
    def _getitem (self,value,cur_node):
        if value>cur_node.value and cur_node.right_child:
            return self._getitem(value,cur_node.right_child)
        elif value<cur_node.value and cur_node.left_child:
            return self._getitem(value,cur_node.left_child)
        if value == cur_node.value:
            return True
        
    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)

    def append(self, value):
        """
        add element in BTS
        """
        if self.root is None:
            self.root = BTSNode(value)
        else: 
            self._append(value,self.root)
            
    def _append(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = BTSNode(value)
            else:
                self._append(value,cur_node.left_child)
        elif value > cur_node.value:   
            if cur_node.right_child is None:
                cur_node.right_child = BTSNode(value)
            else:
                self._append(value,cur_node.right_child)
        else:
            print ("Value in tree")
            
    def __delitem__(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self,node):
        if node==None or self.find(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None 
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current

        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children

        node_parent=node.parent
        node_children=num_children(node)

        if node_children==0:

            if node_parent!=None:
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None

        if node_children==1:
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            if node_parent!=None:

                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child
            child.parent=node_parent

        if node_children==2:

            successor=min_value_node(node.right_child)
            node.value=successor.value

            self.delete_node(successor)
#проверка
tt=BinaryTree()
tt.append (4)
tt.append(10)
tt.append(45)
tt.append(35)
tt.__delitem__(10)
