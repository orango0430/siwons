A=int(input())
B=list(map(int,input().split()))
T,P=map(int,input().split())
result = 0
for i in range(len(B)):
    if B[i] % T == 0:
        result+=B[i]//T
    else:
        result+=(B[i]//T)+1
print(result)
print(A//P, A%P)