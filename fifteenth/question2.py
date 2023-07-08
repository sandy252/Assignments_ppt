def nearest_smaller_numbers(arr):
    stack = []
    result = []

    # Traverse the array to find nearest smaller numbers
    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        
        if stack:
            result.append(arr[stack[-1]])
        else:
            result.append(-1)
        
        stack.append(i)

    return result
