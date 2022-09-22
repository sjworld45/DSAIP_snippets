class Empty(Exception):
    pass
        
class LinkedStack:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, _next):
            self._element = element
            self._next = _next
            
    def __init__(self):
        self._head = None
        self._size = 0
        
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def pop(self):
        if self._head == None:
            raise Empty('Stack is empty')
        tmp = self._head._element
        self._head = self._head._next
        self._size -= 1
        return tmp._element
    
    def top(self):
        if self._head == None:
            raise Empty('Stack is empty')
        return self._head._element
        
    def is_empty(self):
        return self._head == None
        
    def __len__(self):
        return self._size
        
