class Tree_Base:
    
    # nested Position Class
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subClass')
            
        def __eq__(self):
            raise NotImplementedError('must be implemented by subClass')
            
        def __ne__(self, other):
            return not (self == other)
            
    # abstract methods tht concrete subClass must support
    
    def root(self):
        raise NotImplementedError('must be implemented by subClass')
    
    def parent (self, p):
        raise NotImplementedError('must be implemented by subClass')
            
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subClass')
        
    def children(self, p):
        raise NotImplementedError('must be implemented by subClass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subClass')

    # concrete methods implemented in this class
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
        
    def _height2(self, p):
        if self.num_children(p) == 0:
            return 1
        else:
            return 1+max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        if p == None:
            p = self.root()
        return self._height2(p)