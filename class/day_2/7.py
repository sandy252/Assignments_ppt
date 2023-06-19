arr = [1,4,5,9,12]
def palindrom_merger(arr):
    i = 0
    j = len(arr)-1
    counter = 0
    while(i<=j):
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            continue
        if arr[i]>arr[j]:
            arr[j-1] = arr[j]+arr[j-1]
            counter += 1
            j -= 1
        else:
            arr[i+1] = arr[i]+arr[i+1]
            counter += 1
            i += 1
    return counter

print(palindrom_merger(arr))