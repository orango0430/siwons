A=int(input())
result=[]
for i in range(A):
    B,C=(input().split())   
    result.append([int(B),i,C])
result.sort()
for i in range(A):
    print(result[i][0], result[i][2])