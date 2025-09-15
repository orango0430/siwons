import sys
input = sys.stdin.readline
sum = 0
result = []
for i in range(5):
    n = int(input())
    result.append(n)
for j in (result):
    sum += j
avg = sum / 5 
print(int(avg))
result.sort()
print(result[2]) 