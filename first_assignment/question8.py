def find_numbers(arr):
    sum1 = 0
    sum2 = 0
    mini = min(arr)
    maxi = max(arr)
    for i in range(mini, maxi+1):
        sum1 +=i
    for i in range(len(arr)):
        if arr.count(arr[i]) > 1:
            extra = arr[i]
        sum2 += arr[i]
        
    missing = sum1-(sum2-extra)
    return extra, missing
#     return missing,extra

print(find_numbers([1,2,3,3,5]))