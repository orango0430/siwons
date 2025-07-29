A=int(input())
B=int(input())
sum=0
for i in range(B) :
    C,D=map(int,input().split())
    sum += C*D
if A == sum :
    print("Yes")
else:
    print("No")
