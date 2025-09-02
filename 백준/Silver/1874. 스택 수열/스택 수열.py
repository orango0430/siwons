import sys
input = sys.stdin.readline
n = int(input())
m = [int(input()) for _ in range(n)]
s = []
result = []
cnt = 1
for i in (m):
    while cnt <= i :
        s.append(cnt)
        result.append('+')
        cnt+=1
    if s and s[-1] == i:
        s.pop()
        result.append('-')
    else:
        print('NO')
        break
else:
    print('\n'.join(result))