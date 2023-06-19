def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]):
            return mid
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


nums = [1, 2, 3, 1]
peak_index = findPeakElement(nums)
print(peak_index)
