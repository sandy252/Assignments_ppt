def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    pair_sum = 0

    # Pair adjacent elements to maximize the sum of minimums
    for i in range(0, len(nums), 2):
        pair_sum += nums[i]

    return pair_sum

nums = [1, 4, 3, 2,8]
result = arrayPairSum(nums)
print(result)  # Output: 4
