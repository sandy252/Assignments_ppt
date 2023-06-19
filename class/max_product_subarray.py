# def maximum_product_subarray(arr):
#     if len(arr) == 0:
#         return 0
    
#     max_so_far = arr[0]
#     min_so_far = arr[0]
#     result = max_so_far

#     for i in range(1,len(arr)):
#         curr = arr[i]
#         temp_max = max(curr, max(max_so_far * curr, min_so_far *curr))
#         min_so_far = min(curr, min(max_so_far*curr, min_so_far * curr))

#         max_so_far = temp_max
#         result = max(max_so_far, result)
#     return result

# print(maximum_product_subarray([2,3,-2,4]))

# arr = [2,3,-2,4]
arr = [2,3,-2,-5,6,-1,4]


def max_product_subarray(arr):
    n = len(arr)
    left_prod = 1
    right_prod = 1
    ans = arr[0]
    for i in range(len(arr)):
        if left_prod == 0:
            left_prod = 1
        if right_prod == 0:
            right_prod = 1
        
        left_prod *= arr[i]
        right_prod *= arr[n-1-i]
        ans = max(ans, left_prod, right_prod)
    return ans


print(max_product_subarray(arr))