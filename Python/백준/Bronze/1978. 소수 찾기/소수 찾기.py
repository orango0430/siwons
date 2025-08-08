A=int(input())
B=list(map(int,input().split()))
result=[]
for i in B:
    if i<=1:
        result.append(i)
        continue
    for j in range(2,i):
        if i % j == 0:
            result.append(i)
            break
for num in result:
    if num in result:
        B.remove(num)
print(len(B))
