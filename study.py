arr = [5,3,9,7,6,4,1]
def quick_sort(arr,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[start]:
            right -= 1
        if left > right:
            arr[right],arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left],arr[right] = arr[right], arr[left]
    quick_sort(arr,start,right -1)
    quick_sort(arr,right+1,end)
quick_sort(arr,0,len(arr)-1)
print(arr)
