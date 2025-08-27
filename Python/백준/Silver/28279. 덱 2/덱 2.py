from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
q=deque()
result=[]
for _ in range(n):
    a = input().split()
    cmd=a[0]
    if cmd == '1':
        q.appendleft(a[1])
    elif cmd == '2':
        q.append(a[1])
    elif cmd == '3':
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q.popleft()))
    elif cmd == '4':
        if len(q) == 0:
            result.append(str(-1))
        else:
            result.append(str(q.pop()))
    elif cmd == '5':
        result.append(str(len(q)))
    elif cmd == '6':
        if len(q) == 0:
            result.append(str(1))
        else:
            result.append(str(0))
    elif cmd == '7':
        if len(q) == 0:
            result.append(str(-1))
        else: 
            result.append(str(q[0]))
    elif cmd == '8':
        if len(q) == 0 :
            result.append(str(-1))
        else:
            result.append(str(q[-1]))
print('\n'.join(result))
