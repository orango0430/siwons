n = int(input())
s = input().strip()
r = 31
m = 1234567891
count = 0
for i in range(n):
    num = ord(s[i]) - 96
    count += num * r ** i 
print(count%m)
