import sys
input = sys.stdin.readline
t = int(input())
a = [[0]*(15) for _ in range(15)]
for n in range(1, 15):
    a[0][n] = n
for k in range(1,15):
    a[k][1] = 1
    for n in range(2,15):
        a[k][n] = a[k][n-1] + a[k-1][n]
for _ in range(t):
    k = int(input())
    n = int(input())
    print(a[k][n])

