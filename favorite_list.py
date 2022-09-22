from positional_list import PositionalList

class FavoriteList:
    
    class _Item:
        __slots__ = '_name', '_count'
        def __init__(self, e):
            self._name = e
            self._count = 1
            
    def __init__(self):
        self._data = PositionalList()
        
    def __len__(self):
        return len(self._data)
        
    def is_empty(self):
        return len(self) == 0
        
    def _find_pos(self, e):
        walk = self._data.first()
        while walk:
            if walk._element()._name == e:
                return walk
            walk = self._data.after(walk)
        
    def _move_pos(self, p):
        p._element()._count += 1
        pos_below = self._data.before(p)
        if pos_below and p._element()._count > pos_below._element()._count:
            self._data.add_before(pos_below, p._element())
            self._data.delete(p)
            
        
                
                
    def access(self, e):
        p = self._find_pos(e)
        if p:
            val = p._element()._count
            self._move_pos(p)
            return val
        else:
            new_item = self._Item(e)
            self._data.add_last(new_item)
            return new_item._count
            
    def remove(self, e):
        p = self._find_pos(e)
        if p:
           self._data.delete(p)
            
    def top(self, k):
        i = 0
        for e in self._data:
            i += 1
            name = e._name
            count = e._count
            print(f'{name}: {count}')
            if i==k:
                break