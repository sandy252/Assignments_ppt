def find132pattern(nums):
    n = len(nums)
    if n < 3:
        return False

    stack = []
    max_k = float('-inf')

    for i in range(n-1, -1, -1):
        if nums[i] < max_k:
            return True
        while stack and nums[i] > stack[-1]:
            max_k = stack.pop()
        stack.append(nums[i])

    return False
