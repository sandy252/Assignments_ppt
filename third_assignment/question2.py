def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    result = []

    for a in range(n-3):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        for b in range(a+1, n-2):
            if b > a+1 and nums[b] == nums[b-1]:
                continue
            left = b + 1
            right = n - 1
            while left < right:
                curr_sum = nums[a] + nums[b] + nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[a], nums[b], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

    return result
