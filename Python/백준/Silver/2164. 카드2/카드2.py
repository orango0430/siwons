from collections import deque
n=int(input())
s=deque(range(1,n+1))
while len(s) > 1:
    s.popleft()
    s.append(s.popleft())
print(s[0])