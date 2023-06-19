def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = []

    for num in nums2:
        if num in set1:
            intersection.append(num)
            set1.remove(num)

    return intersection


print(intersection([4, 9, 5], [9, 4, 9, 8, 4])) 
