def sortColors(nums):
    low = 0    # pointer for red section
    mid = 0    # pointer for white section
    high = len(nums) - 1    # pointer for blue section

    while mid <= high:
        if nums[mid] == 0:    # current element is red
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:  # current element is white
            mid += 1
        else:                 # current element is blue
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
