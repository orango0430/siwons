n = (input())
num = [int(x) for x in str(n)]
num.sort(reverse=True)
print(*num,sep='')
