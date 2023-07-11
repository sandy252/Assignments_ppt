# 25. Write a Python program to merge two sorted lists into a single sorted list.
def merger(ls1, lst2):
    # print(ls1)
    # print(lst2)
    ls1.extend(lst2)
    ls1.sort()
    return ls1

print(merger([1,2,3,8,10],[4,6,9]))