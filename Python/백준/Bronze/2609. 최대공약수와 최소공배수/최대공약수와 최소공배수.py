n,m = map(int,input().split())
def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a
s = (n*m) // gcd(n,m)
print(gcd(n,m))
print(s)
