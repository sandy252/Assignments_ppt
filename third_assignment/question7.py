def findMissingRanges(nums, lower, upper):
    result = []
    current = lower

    for num in nums:
        if num < current:
            continue
        if num == current:
            current += 1
            continue
        if num > current:
            result.append([current, num - 1])
            current = num + 1

    if current <= upper:
        result.append([current, upper])

    return result

print(findMissingRanges([0,1,3,50,75],0,99))