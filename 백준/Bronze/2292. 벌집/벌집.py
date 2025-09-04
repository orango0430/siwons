import sys
input = sys.stdin.readline
n = int(input())
def f(x):
    return 3*x*x - 3*x + 1
i = 1
while f(i) < n:
    i+=1
print(i) 