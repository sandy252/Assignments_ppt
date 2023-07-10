def maximumGap(nums):
    if len(nums) < 2:
        return 0

    # Find the maximum element in the array
    max_num = max(nums)

    # Perform Radix Sort on the array
    exp = 1
    while max_num // exp > 0:
        counting_sort(nums, exp)
        exp *= 10

    # Calculate the maximum difference between successive elements
    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i-1])

    return max_diff

def counting_sort(nums, exp):
    n = len(nums)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit at the current digit place
    for i in range(n):
        digit = nums[i] // exp % 10
        count[digit] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the sorted array
    for i in range(n-1, -1, -1):
        digit = nums[i] // exp % 10
        output[count[digit] - 1] = nums[i]
        count[digit] -= 1

    # Copy the sorted array back to the original array
    for i in range(n):
        nums[i] = output[i]
