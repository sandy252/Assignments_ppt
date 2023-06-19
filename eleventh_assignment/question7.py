def searchRange(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    start, end = -1, -1

    # Find leftmost position
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Find rightmost position
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            end = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [start, end]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]
