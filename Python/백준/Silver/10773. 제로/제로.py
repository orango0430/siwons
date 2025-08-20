import sys
class Stack:
    def __init__(self):
        self.storage=[]
    def pop(self):
        return self.storage.pop()
    def total(self):
        return sum(self.storage)
s=Stack()            
k=int(sys.stdin.readline())
for _ in range(k):
    a=int(sys.stdin.readline())
    if a != 0:
        s.storage.append(a)
    else:
        s.pop() 
print(s.total())