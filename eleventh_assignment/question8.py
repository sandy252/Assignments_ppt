from collections import Counter

def intersect(nums1, nums2):
    # Create hash maps for nums1 and nums2
    count1 = Counter(nums1)
    result = []

    # Iterate through nums2
    for num in nums2:
        # Check if num is present in count1 and its frequency is greater than zero
        if num in count1 and count1[num] > 0:
            result.append(num)
            count1[num] -= 1

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersection = intersect(nums1, nums2)
print(intersection)