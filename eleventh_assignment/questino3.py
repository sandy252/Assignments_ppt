def missingNumber(nums):
    n = len(nums)
    missing = n

    for i, num in enumerate(nums):
        missing ^= num ^ i

    return missing

print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
