arr = [29, 10, 14, 37, 13]
for i in range(1, len(arr)): # 두 번째 원소부터 시작
    key = arr[i] # 현재 삽입할 값
    j = i-1
    while (j >= 0 and arr[j] > arr[j+1]):
        arr[j+1] = arr[j]
        j -= 1

        arr[j+1] = key
print(arr)
    