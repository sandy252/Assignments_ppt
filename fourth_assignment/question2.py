nums1 = [1,2,3]
nums2 = [2,4,6]

def func(num1, num2):
    l = []
    j = []
    k = []
    for e in num1:
        if e not in num2:
            j.append(e)
    l.append(j)
    # j.clear()
    for e in num2:
        if e not in num1:
            k.append(e)
    l.append(k)
    # j.clear()
    return l

print(func(nums1,nums2))