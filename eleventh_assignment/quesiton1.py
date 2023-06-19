def mySqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


print(mySqrt(16))  
print(mySqrt(8))   
