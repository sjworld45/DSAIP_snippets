from favorite_list import FavoriteList

class FavoriteListMTF(FavoriteList):
    
    def _move_up(self, p):
        if p != self._data.first()
            self._data.add_first(self._data.delete(p))
            
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal val for k')
            
        temp = list()
        for item in self._data:
            temp.append(item)
            
        temp.sort(key = lambda e: e._count, reverse = True)
        
        for i in range(k):
            yield temp[i]
            
        del temp
            