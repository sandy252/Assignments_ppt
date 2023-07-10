def max_subarray_sum_circular(nums):
    max_sum = float('-inf')
    min_sum = float('inf')
    array_sum = 0

    for num in nums:
        array_sum += num
        max_sum = max(num, max_sum + num)
        min_sum = min(num, min_sum + num)

    if array_sum == min_sum:
        return max_sum

    max_sum_no_wrap = array_sum - min_sum

    array_sum = 0
    max_sum = float('-inf')

    for num in nums:
        array_sum += num
        if array_sum < 0:
            array_sum = 0
        max_sum = max(max_sum, array_sum)

    return max(max_sum, max_sum_no_wrap)
