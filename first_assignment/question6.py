def isvalid(arr):
    dict = {}
    for i in arr:
        count = 0
        if i in dict.keys():
            return False
        if i not in dict.keys():
            dict[1] = 1
    return True

print(isvalid([1,2,3]))