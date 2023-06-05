def shuffle(nums, n):
    x = nums[:n]  # First half of the array
    y = nums[n:]  # Second half of the array

    shuffled = []

    
    for i in range(n):
        shuffled.append(x[i])
        shuffled.append(y[i])

    return shuffled

nums = [2,5,1,3,4,7]
n = 3
result = shuffle(nums, n)
print(result) 
