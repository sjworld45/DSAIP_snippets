class Empty(Exception):
    pass

class Node:
    def __init__(self, element, nxt = None):
        self._element = element
        self._next = nxt
        
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None
    
    def add_head(self, node):
        node._next = self._head
        self._head = node
        self._size += 1
        if self._size == 1:
            self._tail = self._head
        
    def add_tail(self, node):
        self._tail._next = node
        self._tail = node
        self._size += 1
    
    def remove_head(self):
        if self._size == 0:
            raise Empty('No nodes in Linked List')
        node = self._head
        self._head = self._head._next
        self._size -= 1
        return node
        
    def remove_tail(self):
        if self._size == 0:
            raise Empty('No nodes in linked list')
        node = self._head
        prev = node
        while node._next:
            prev = node
            node = node._next
        self._tail = prev
        prev._next = None
        self._size -= 1
        return node
    
    def head(self):
        if self._size == 0:
            raise Empty('No nodes in Linked list')
        return self._head 
        
    def tail(self):
        if self._size == 0:
            raise Empty('No nodes in Linked list')
        return self._tail
        
        
    def __len__(self):
        return self._size
        
    def traverse(self, node=None):
        if node==None:
            node = self._head
            
        while node._next:
            print(node._element)
            node = node._next
        else:
            print(node._element)
        

        
            