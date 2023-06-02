def nextPermutation(nums):
    n = len(nums)
    pivot_index = -1

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            pivot_index = i
            break

    # If no pivot is found, array is sorted in descending order
    if pivot_index == -1:
        nums.reverse()
        return nums

    # Find the element to swap with the pivot
    for i in range(n-1, pivot_index, -1):
        if nums[i] > nums[pivot_index]:
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            break

    # Reverse the subarray from pivot_index+1 to the end
    nums[pivot_index+1:] = reversed(nums[pivot_index+1:])

    return nums
print(nextPermutation([1,2,3]))