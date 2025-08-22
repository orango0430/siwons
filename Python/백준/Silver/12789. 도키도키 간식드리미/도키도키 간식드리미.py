import sys
n=int(sys.stdin.readline())
m=list(map(int,sys.stdin.readline().split()))
stack=[]
num=1
idx=0
result='Nice'
while idx < len(m):
    if m[idx] == num:
        num+=1
        idx+=1
    elif stack and stack[-1] == num:
        stack.pop()
        num+=1
    else:
        stack.append(m[idx])
        idx+=1
while stack:
    if stack[-1] == num:
        stack.pop()
        num+=1
    else:
        result='Sad'
        break
print(result)