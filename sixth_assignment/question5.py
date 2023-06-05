def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    min_product_sum = 0

    for i in range(len(nums1)):
        min_product_sum += nums1[i] * nums2[i]

    return min_product_sum

print(minProductSum([5,3,4,2],[4,2,2,5]))