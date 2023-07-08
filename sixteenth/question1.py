def findNearestGreaterFrequency(nums):
    frequency = {}
    stack = []
    nearest = [-1] * len(nums)

    # Calculate the frequency of each element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Traverse the array from right to left
    for i in range(len(nums) - 1, -1, -1):
        while stack and frequency[nums[i]] >= frequency[nums[stack[-1]]]:
            stack.pop()

        if stack:
            nearest[i] = nums[stack[-1]]

        stack.append(i)

    return nearest
