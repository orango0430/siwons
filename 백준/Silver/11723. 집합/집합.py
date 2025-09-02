import sys
input = sys.stdin.readline
write = sys.stdout.write
n = int(input())
mask = 0
ALL = (1<<21) -2
for _ in range(n):
    m = input().split()
    cmd = m[0]
    if cmd == 'add':
        x = int(m[1]); mask |= (1<<x)
    elif cmd == 'remove':
        x = int(m[1]); mask &= ~(1<<x)
    elif cmd == 'check':
        x = int(m[1]); write('1\n'if (mask & (1<<x)) else '0\n')
    elif cmd == 'toggle':
        x = int(m[1]); mask ^= (1<<x) 
    elif cmd == 'all':
        mask = ALL
    else :  
        mask = 0