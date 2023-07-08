def trap_water(heights):
    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left <= right:
        if heights[left] <= heights[right]:
            if heights[left] > left_max:
                left_max = heights[left]
            else:
                total_water += left_max - heights[left]
            left += 1
        else:
            if heights[right] > right_max:
                right_max = heights[right]
            else:
                total_water += right_max - heights[right]
            right -= 1

    return total_water
