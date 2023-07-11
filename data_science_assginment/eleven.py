#  11. Write a program to find the common elements between two lists.

def find_common(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    return s1.intersection(s2)

print(find_common([1,2,3,4,5],[2,3,4]))