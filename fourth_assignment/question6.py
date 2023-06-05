def sortedSquares(nums):
    squared_nums = [num**2 for num in nums]  # Square each element
    squared_nums.sort()  # Sort the squared values
    return squared_nums


nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)  
