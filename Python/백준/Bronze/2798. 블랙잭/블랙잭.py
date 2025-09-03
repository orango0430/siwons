import sys
import itertools
input = sys.stdin.readline
n,m = map(int,input().split())
s = list(map(int,input().split()))
best = 0
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = s[i] + s[j] + s[k]
            if sum <= m and sum > best:
                best = sum
                
print(best)