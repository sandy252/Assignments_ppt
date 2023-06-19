def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[left] <= nums[mid] <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    return nums[left]


nums = [4, 5, 6, 7, 0, 1, 2]
minimum = findMin(nums)
print(minimum)
