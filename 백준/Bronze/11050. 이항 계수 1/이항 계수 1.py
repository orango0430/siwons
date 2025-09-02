import math
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
s = math.comb(n,k)
print(s)