from collections import deque
n, k=map(int, input().split())
q=deque(range(1,n+1))
result=[]
while len(q) >= 1:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
print('<',end='')
print(*result,sep=', ',end='')
print('>')