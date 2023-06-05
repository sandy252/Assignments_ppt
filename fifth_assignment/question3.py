def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    idx = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[idx] = nums[left] ** 2
            left += 1
        else:
            result[idx] = nums[right] ** 2
            right -= 1
        idx -= 1

    return result


nums = [-4, -2, 0, 3, 10]
result = sortedSquares(nums)
print(result)  