class Empty(Exception):
    pass

class Stack:
    def __init__(self, t = None):
        if t:
            self._A = list(t)
            self._n = len(list(t))
        else:
            self._A = []
            self._n = 0
        
    def push(self, e):
        self._A.append(e)
        self._n += 1
    
    def pop(self):
        if self._n == 0:
            raise Empty('Stack is Empty')
        self._n -=1 
        return self._A.pop()
        
    def top(self):
        if self._n == 0:
            raise Empty('Stack is Empty')
        return self._A[self._n-1]
    
    def is_empty(self):
        return self._n == 0
    
    def __len__(self):
        return self._n
        
    def __str__(self):
        return str(self._A)
        
def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


def main():
    S = Stack(range(10))
    print(S.top())
    temp1  = Stack()
    temp2  = Stack()
    transfer(S, temp1)
    transfer(temp1, temp2)
    transfer(temp2, S)

    print(S.top())
    
if __name__ == '__main__':
    main()