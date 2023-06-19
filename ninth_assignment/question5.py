def findMax(arr, start, end):
    if start == end:
        return arr[start]
    
    mid = (start + end) // 2
    left_max = findMax(arr, start, mid)
    right_max = findMax(arr, mid + 1, end)
    
    return max(left_max, right_max)


arr = [5, 2, 9, 1, 7]
max_element = findMax(arr, 0, len(arr) - 1)
print(max_element)  
