import sys
n=int(sys.stdin.readline())
num1=set(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
num2=list(map(int,sys.stdin.readline().split()))
for i in num2 :
    if i in num1:
        print('1')
    else:
        print('0')