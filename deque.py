class Empty(Exception):
    pass
    
class Deque:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._A = [None]*self.DEFAULT_CAPACITY
        self._first = 0
        self._size = 0
        
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def __len__(self):
        return self._size
        
    def _check_empty(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        
    def add_first(self, e):
        if self._size == len(self._A):
            self._resize(2*self._size)
        if self._size == 0:
            self._A[0] = e
            self._first = 0
        else:
            self._first = (self._first-1)%len(self._A)
            self._A[self._first] = e
        self._size += 1
        
    def add_last(self, e):
        if self._size == len(self._A):
            self._resize(2*self._size)
            
        if self._size == 0:
            self._A[0] = e
            self._first = 0
        else:
            ind = (self._first + self._size-1)%len(self._A)
            self._A[ind] = e
        self._size += 1
        
    def delete_first(self):
        self._check_empty()
            
        val = self._A[self._first]
        self._first = (self._first + 1) % len(self._A)
        self._size -= 1
        return val
        
    def delete_last(self):
        self._check_empty()
        
        ind = (self._first + self._size-1)%len(self._A)
        val = self._A[ind]
        self._size -= 1
        return val
        
    def first(self):
        self._check_empty()
        return self._A[self._first]
        
    def last(self):
        self._check_empty()
        ind = (self._first+self._size-1)%len(self._A)
        return self._A[ind]
        
        
        
    def _resize(self, cap):
        temp = [None]*cap
        for i in range(self._size):
            temp[i] = self._A[self._first]
            self._first = (self._first+1)%self._size
            
        self._first = 0
        self._A = temp