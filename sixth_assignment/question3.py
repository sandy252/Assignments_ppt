def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False
    
    i = 1
    while i < n and arr[i] > arr[i-1]:
        i += 1
    
    if i == 1 or i == n:
        return False
    
    while i < n and arr[i] < arr[i-1]:
        i += 1
    
    return i == n


print(validMountainArray([2,1]))