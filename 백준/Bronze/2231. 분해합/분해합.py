import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for i in range(1,n+1):
    num = list(map(int,str(i)))
    cnt = sum(num)+i
    if cnt == n:
        print(i)
        break
    if i == n:
        print('0')

    