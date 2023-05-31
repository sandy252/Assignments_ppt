def array_pair_sum(nums):
    nums.sort()  
    for i in range(0, len(nums), 2):  
        sum_min += nums[i]  

    return sum_min

print(array_pair_sum([1,4,3,2]))