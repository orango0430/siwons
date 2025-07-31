lst=[1,1,2,2,2,8]
A=list(map(int,input().split())) 
diff=[]
for i in range(len(lst)):
    C=lst[i]-A[i]
    diff.append(C)
print(*diff)