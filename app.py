arr = [29, 10, 14, 37, 13]
for i in range(1, len(arr)): # 두 번째 원소부터 시작
    key = arr[i] # 현재 삽입할 값 (비교 대상자)
    j = i-1 
    while (j >= 0 and arr[j] > arr[j+1]): #'key' 보다 큰 원소는 한 칸씩 오른쪽으로 이동
        arr[j+1] = arr[j] #원소 교환
        j -= 1 #다시 왼쪽이랑 비교

        arr[j+1] = key #올바른 위치에 삽입할 값 삽입
print(arr)
    
