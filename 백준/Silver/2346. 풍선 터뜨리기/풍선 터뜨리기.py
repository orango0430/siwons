from collections import deque
import sys
input=sys.stdin.readline
n = int(input())
q = deque(enumerate(map(int, input().split()))) 
result=[]
idx = 1
while q:
    for _ in range(abs(idx)-1): # idx값 절댓값 처리
        if idx < 0:
            q.appendleft(q.pop())
        else:
            q.append(q.popleft()) 
    if idx < 0 :
        num, idx = q.pop()
    else:
        num, idx = q.popleft()
    num+=1
    result.append(num)
print(*result)