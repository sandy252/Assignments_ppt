def findMaxLength(nums):
    count_dict = {0: -1}  
    max_length = 0
    count = 0

    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1

        if count in count_dict:
            length = i - count_dict[count]
            max_length = max(max_length, length)
        else:
            count_dict[count] = i

    return max_length

print(findMaxLength([0,1]))