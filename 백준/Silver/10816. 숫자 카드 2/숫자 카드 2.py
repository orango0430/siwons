import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int,input().split()))
m = int(input())
k = list(map(int,input().split()))
d = dict()
for i in (s):
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in (k):
    if i in d:
        print(d[i], end=' ')
    else:
        print(0, end=' ')