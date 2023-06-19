def missing_no(arr):
    s = set(arr)
    for i in range(len(arr)):
        if i not in s:
            return i
    return "All present"


print(missing_no([0,1,2,3,4,5]))