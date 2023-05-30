def find_index(arr, key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
            break
        elif key < arr[mid] :
            high = mid-1
        else:
            low = mid+1
    
print(find_index([1,3,5,6], 5))