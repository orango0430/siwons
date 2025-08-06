import sys
A=int(sys.stdin.readline())
N=[]
for i in range(A):
    B,C=map(int,sys.stdin.readline().split())
    N.append([B,C])
N.sort()
for i in range(A):
    print(N[i][0], N[i][1])