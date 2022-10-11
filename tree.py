from tree_base_class import Tree_Base
from linked_queue import LinkedQueue

class Tree(Tree_Base):
    
    class _Node:
        # __slots__ = '_element', '_parent', '_children'
        
        def __init__(self, parent, e):
            self._element = e
            self._parent = parent
            self._children = []
            
        def _add_child(self, n):
            self._children.append(n)
            
        def _remove_child(self, n):
            for i in range(len(self._children)):
                if self._children[i] == n:
                    self._children.pop(i)
                    break
                        
            
            
    def __init__(self, e = None):
        self._root = None
        self._size = 0
        
    def add_node(self, e, parent = None):
        if parent is None:
            self._root = self._Node(None, e)
            val = self._root
        else:
            val = self._Node(parent, e)
            parent._add_child(val)
        self._size += 1
        return val
        
    def edit_node(self, node, e):
        node._element = e
    
    def remove_node(self, n, parent):
        parent._remove_child(n)
        self._size += 1
        
    def children(self, node):
        return node._children
        
    def __len__(self):
        return self._size
        
    def positions(self):
        return self.preorder()
        
    def __iter__(self):
        for p in self.positions():
            yield p.element()
            
    
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
        
    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
                
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
                
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
        
    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
                    
    def preorder_indent(T, p, d):
        print(2*d*' ' + str(p.element())
        for c in T.children(p):
            preorder_indent(T, c, d+1)
        
    def preorder_label(T, p, d, path):
        label = '.'join(str(j+i) for j in path)
        print(2*d*' '+label, p.element())
        path.append(0)
        for c in T.children(p):
            preorder_label(T, c, d+1, path)
            path[-1] += 1
        path.pop()
        
        
    def parenthesize(T, p):
        print(p.element(), end = '')
        if not T.is_leaf(p):
            first_time = True
            for c in T.children(p):
                sep = 'C' if first_time else ','
                print(sep, end = '')
                first_time = False
                parenthesize(T, c)
            print(')', end = '')