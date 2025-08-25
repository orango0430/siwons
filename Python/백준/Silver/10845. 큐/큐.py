import sys
n=int(sys.stdin.readline())
s=[]
result=[]
for _ in range(n):
    a=sys.stdin.readline().split()
    if a[0] == 'push':
        s.append(a[1])
    elif a[0] == 'pop':
        if len(s) == 0:
            result.append(str(-1))
        else:
            result.append(str(s.pop(0)))            
    elif a[0] == 'size':
        result.append(str(len(s)))
    elif a[0] == 'empty':
        if len(s) == 0:
            result.append(str(1))
        else:
            result.append(str(0))
    elif a[0] == 'front':
        if len(s) == 0:
            result.append(str(-1))
        else:
            result.append(str(s[0]))
    elif a[0] == 'back':
        if len(s) == 0:
            result.append(str(-1))
        else:
            result.append(str(s[-1]))
print('\n'.join(result))

        
