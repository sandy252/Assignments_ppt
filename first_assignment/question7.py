def move_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            temp = arr.pop(i)
            arr.append(temp)
    return arr
    
print(move_zeros([0,1,0,2,12]))