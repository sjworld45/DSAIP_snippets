class Empty(Exception):
    pass

class CircularQueue:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, el, nxt):
            self._element = el
            self._next = nxt
            
    
    def __init__(self):
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._next._element
        
    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._element
        
    def rotate(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        self._tail = self._tail._next
        
    def enqueue(self, e):
        node = self._Node(e, None)
        if self.is_empty():
            node._next = node
        else:
            node._next = self._tail._next
        self._tail = node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        
        ans = self._tail._next
        self._tail._next = ans._next
        
        if self._size == 1:
            self._tail = None
        
        self._size -= 1
        return ans
        
    