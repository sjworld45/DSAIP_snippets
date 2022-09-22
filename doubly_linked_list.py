#without sentinels
class Empty(Exception):
    pass
    
class DoublyLinkedList:
    
    class _Node:
        __slots__ = '_element', '_next', '_prev'
        
        def __init__(self, element, nxt, prv):
            self._element = element
            self._next = nxt
            self._prev = prv
            
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def _check_empty(self):
        if self.is_empty():
            raise Empty('List is empty')
        
    def add_head(self, e):
        node = self._Node(e, self._head, None)
        if self.is_empty():
            self._head = node
            self._tail = node
        
        else:
            self._head._prev = node
            self._head = node
        
        self._size += 1
    
    def add_tail (self, e):
        node = self._Node(e, None, self._tail)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        self._size += 1
    
    
    def remove_head(self):
        self._check_empty()
        ans = self._head._element
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            self._head._next._prev = None
            self._head = self._head._next
            self._size -= 1
        return ans
            
    def remove_tail(self):
        self._check_empty()
        ans = self._tail._element
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            self._tail._prev._next = None
            self._tail = self._tail._prev
            self._size -= 1
        return ans
        
    def remove(self, n):
        '''
        removes node at position n
        '''
        if n >= self._size:
            raise IndexError(f'{n} exceed the current size of list: {self._size}')
        
        if n==0:
            return self.remove_head()
        elif n==self._size-1:
            return self.remove_tail()
        else:
            if n < self._size-n-1:
                i = 0
                node = self._head
                while i<n:
                    node = node._next
                    i += 1
            else:
                i = self._size-1
                node = self._tail
                while i>n:
                    node = node._prev
                    i -= 1
            node._prev._next = node._next
            node._next._prev = node._prev
            
        self._size -= 1
        return node._element
        
    def add(self, n):
        '''
        adds node to position n
        '''
        pass
                
            
            
    def first(self):
        self._check_empty()
        return self._head._element
        
    def last(self):
        self._check_empty()
        return self._tail._element