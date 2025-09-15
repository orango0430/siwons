import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    k = int(input())
    nums.append(k)
nums.sort()
for i in nums:
    print(i)