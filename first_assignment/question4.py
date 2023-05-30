def increment_integer(arr):
    carry =1
    for i in range(len(arr)-1,-1,-1):
        arr[i] += carry
        
        if arr[i] >= 10:
            arr[i] = arr[i] % 10
            carry = 1
        else:
            carry = 0
            break
    return arr
        
print(increment_integer([1,2,9]))