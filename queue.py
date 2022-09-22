class Empty(Exception):
    pass

class Queue:
    def __init__(self):
        self._A = [None]
        self._size = 0
        self._first = 0
        
    def enqueue(self, e):
        if self._size == len(self._A):
            self._resize(self._size * 2)
            
        ind = (self._first + self._size)%len(self._A)
        self._A[ind] = e
        self._size += 1
     
    def dequeue(self):    
        if self.is_empty():
            raise Empty('Queue is empty')
            
        val = self._A[self._first]
        self._first = (self._first + 1)%len(self._A)
        self._size -= 1
        return val
        
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
        
        
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._A[self._first]
        
    def __len__(self):
        return self._size 
        
    def _resize(self, cap):
        temp = [None]*cap
        f = self._first
        i = 0
        while i<self._size:
            temp[i] = self._A[f]
            f = (f+1)%len(self._A)
            i += 1
            
        self._first = 0
        self._A = temp
        
