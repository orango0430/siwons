a, b, v = map(int, input().split())
d = a - b
print((v - b + d - 1 ) // d)
