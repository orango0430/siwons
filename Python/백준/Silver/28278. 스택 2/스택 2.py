class Stack:
    def __init__(self):
        self.storage=[]
    def pop(self):
        if len(self.storage) == 0:
            return -1
        else:
            return self.storage.pop()
    def size(self):
            return len(self.storage)
    def empty(self):
        if len(self.storage) == 0:
            return 1 
        else: 
            return 0
    def top(self):
        if len(self.storage) == 0:
            return -1
        else :
            return self.storage[-1]
import sys
s=Stack()
n=int(sys.stdin.readline())
result=[]
for _ in range(n):
    x=(sys.stdin.readline().split())    
    if x[0] == '1':
        s.storage.append(int(x[1]))
    elif x[0] == '2':
        result.append(str(s.pop()))
    elif x[0] == '3':
       result.append(str(s.size()))
    elif x[0] == '4':
        result.append(str(s.empty()))
    elif x[0] == '5':
        result.append(str(s.top()))
print('\n'.join(result))
    
     
