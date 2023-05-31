def minimumScore(nums, k):
    nums.sort()
    n = len(nums)
    
    min_score = nums[n-1] - nums[0]
    
    for i in range(1, n):
        new_min = min(nums[0] + k, nums[i] - k)
        new_max = max(nums[i-1] + k, nums[n-1] - k)
        
        min_score = min(min_score, new_max - new_min)
    
    return min_score

print(minimumScore([1], 0))
