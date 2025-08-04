A=int(input())
B=list(map(int,input().split()))
T,P=map(int,input().split())
result = 0
for i in range(len(B)):
    result+=(B[i]+T-1)//T
print(result)
print(A//P, A%P)