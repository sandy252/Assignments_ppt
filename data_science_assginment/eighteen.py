# 18. Implement a function to find the maximum subarray sum in a given list.
def maxsubarraysum(arr):
    maxsum = 0
    cursum = 0
    for i in range(len(arr)):
        cursum = cursum + arr[i]
        if cursum > maxsum:
            maxsum = cursum
        if cursum < 0:
            cursum = 0
    return maxsum


print(maxsubarraysum([5,-4,-2,6,-1]))