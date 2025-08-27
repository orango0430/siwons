result=[]
while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]: # 리스트로 입력받아서 뒤집는게 아니라 문자열로 뒤집는게 깔끔
        result.append('yes')
    else:
        result.append('no')

print('\n'.join(result))
