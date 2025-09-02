import sys
input = sys.stdin.readline
n = int(input())
x = [list(map(int,input().split())) for _ in range(n)]
s = []
for i in range(n):
    k = 1
    for j in range (n):
        if i == j:
            continue
        if x[i][0] < x[j][0] and x[i][1] < x[j][1]:
            k+=1
    s.append(k)
print(*s)