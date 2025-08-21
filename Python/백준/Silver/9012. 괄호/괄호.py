class Stack:
    def __init__(self):
        self.storage=[]
    def push(self,val):
        self.storage.append(val)
    def pop(self):
       if len(self.storage) != 0:
           return self.storage.pop()
       else:
           return None
    def empty(self):
         return len(self.storage) == 0
                       
k=int(input())
m=[]
for _ in range(k):
    a=(input())
    s=Stack()
    answer = True
    for i in a:
        if i == '(':
            s.push(i)
        else:
            if s.empty():
                answer = False
                break
            else:
                s.pop()
                answer = True
    if not s.empty():
        answer = False
    if answer == True:
        m.append("YES")
    else:
        m.append("NO")
print('\n'.join(m))
    