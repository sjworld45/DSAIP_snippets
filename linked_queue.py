class Empty(Exception):
    pass
    
class LinkedQueue:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, _next):
            self._element = element
            self._next = _next
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size += 1
        
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
        
    def enqueue(self, e):
        node = self._Node(e, None)
        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1
        
        
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        
        ans = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans._element
        
        