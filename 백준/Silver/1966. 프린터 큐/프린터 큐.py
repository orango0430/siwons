from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split()) # n은 문서의 개수, m은 몇번째로 인쇄되었는지 궁금한 문서의 현 위치
    result = list(map(int, input().split())) # 문서의 중요도
    q = deque()
    for i, x in enumerate(result): # x == 중요도, i == 문서의 현 위치
        q.append((i,x))
    result.sort() 
    cnt = 0
    answer=[]
    while q:
        i, x = q.popleft()
        if x == result[-1]:
            result.pop()
            cnt+=1
            if i == m:
                print(cnt)
                break
        else:
            q.append((i,x))
        