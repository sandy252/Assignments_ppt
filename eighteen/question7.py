def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    # Initialize an array to store the lengths of the increasing subsequences
    dp = [1] * n

    # Iterate through the array to compute the lengths of the increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Find the maximum length of the increasing subsequence
    max_length = max(dp)

    return max_length
