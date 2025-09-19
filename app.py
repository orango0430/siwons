arr = [29, 10, 14, 37, 13]
for i in range(len(arr)):
    min_idx = i # 최솟값의 인덱스 
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]: 
             min_idx = j 
    arr[i], arr[min_idx] = arr[min_idx], arr[i] # 교환할때는 i로 교환
print(arr)
            
    
        

