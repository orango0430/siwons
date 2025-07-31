A=int(input())
B=list (map(int,input().split()))
M=max(B)
B=list(map(lambda x:x/M*100,B))
total=sum(B)
result=total/A
print(result)


