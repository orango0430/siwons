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
m=[]                     
while True:
    a=input().rstrip('\n')
    if a == ".":
        break
    s=Stack()
    answer=True
    for i in a:
        if i == '[' or i == '(':
            s.push(i)
        elif i == ']' or i ==')':
            if s.empty():
                answer=False
                break
            top = s.pop()
            if(i == ')'and top != '(') or (i == ']' and top != '['):
                answer=False 
                break   
            else:
                continue          
    if not s.empty():
        answer=False
    if answer == True:
        m.append("yes")
    else:
        m.append("no")
print('\n'.join(m))    
           
        