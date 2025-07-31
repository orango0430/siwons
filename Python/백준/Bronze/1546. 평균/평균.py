import sys
A=int(sys.stdin.readline().strip())
B=list (map(int,sys.stdin.readline().split()))
M=max(B)
B=list(map(lambda x:x/M*100,B))
total=sum(B)
result=total/A
print(result)


