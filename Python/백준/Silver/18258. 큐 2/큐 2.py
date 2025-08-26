from collections import deque
import sys
n=int(sys.stdin.readline())
q=deque()
result=[]
for i in range(n):
    a=sys.stdin.readline().split()
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q.popleft()))
    elif a[0] == 'size':
        result.append(str(len(q)))
    elif a[0] == 'empty':
        if len(q) == 0:
            result.append(str(1))
        else:
            result.append(str(0))
    elif a[0] == 'front':
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q[0]))
    elif a[0] == 'back':
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q[-1]))
print('\n'.join(result))    
        
    