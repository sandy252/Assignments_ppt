def findDistanceValue(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        has_close_element = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                has_close_element = True
                break
        if not has_close_element:
            distance += 1

    return distance


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
result = findDistanceValue(arr1, arr2, d)
print(result)  
