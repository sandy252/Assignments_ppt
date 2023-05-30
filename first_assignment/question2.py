def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

nums = [3, 2, 2, 3]
val = 3
k = remove_element(nums, val)
print(k)  