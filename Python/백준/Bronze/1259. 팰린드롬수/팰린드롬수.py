result=[]
while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        result.append('yes')
    else:
        result.append('no')
print('\n'.join(result))