import sys
def my_round(num): # 파이썬에서 round는 오사오입이라 직접구현
    return int(num+0.5)
n=int(sys.stdin.readline())
result=[int(sys.stdin.readline()) for _ in range(n)]
if n == 0:
    print('0')
else:
    result.sort()
    m=my_round(n*0.15) # 직접구현 함수로 15% 계산
    new=result[m:n-m] # 리스트에서 정렬 후 최소 15% 최대 15% 계산
    avg=sum(new)/len(new) 

    print(my_round(avg))
