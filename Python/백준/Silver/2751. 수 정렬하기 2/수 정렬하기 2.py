import sys
A=int(sys.stdin.readline())
nums=[]
for i in range(A):
    B=int(sys.stdin.readline())
    nums.append(B)
nums.sort()
for i in nums:
    print((i))
