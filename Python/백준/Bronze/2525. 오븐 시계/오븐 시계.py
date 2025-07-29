H,M=map(int,input().split())
X = int(input())
M+=X
if M >= 60:
    H+=(M)//60
    M=(M)%60
if H >= 24:
    H=H%24
print(H,M)