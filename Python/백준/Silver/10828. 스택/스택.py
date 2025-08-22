class Stack:
    def __init__(self):
        self.storage=[]
    def push(self, x):
        return self.storage.append(x)
    def pop(self):
        if self.storage:
            return self.storage.pop()
        else:
            return -1
    def size(self):
        return len(self.storage)
    def empty(self):
        if len(self.storage) == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.storage:
            return self.storage[-1]
        else:
            return -1    
n=int(input())
s=Stack()
result=[]
for _ in range(n):
    a=input().split()
    if a[0] == 'push':
        s.push(a[1])
    elif a[0] == 'pop':
        result.append(str(s.pop()))
    elif a[0] == 'size':
        result.append(str(s.size()))
    elif a[0] == 'empty':
        result.append(str(s.empty()))
    elif a[0] == 'top':    
        result.append(str(s.top()))
print('\n'.join(result)) 
    
