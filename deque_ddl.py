from doubly_linked_with_sentinels import _DoublyLinkedBase
from doubly_linked_with_sentinels import Empty

class LinkedDeque(_DoublyLinkedBase):
    
    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)
        
    def add_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    
    def _check_empty(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        
    def remove_first(self):
        self._check_empty()
        self._delete_node(self._header._next)
        
    def remove_last(self):
        self._check_empty()
        self._delete_node(self._trailer._prev)
        
    def first(self):
        self._check_empty()
        return self._header._next._element
        
    def last(self):
        self._check_empty()
        return self._trailer._prev._element
