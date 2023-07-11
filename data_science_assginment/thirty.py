#  30. Implement a function to find the minimum element in a rotated sorted list.
# ans will be not in unsorted part
# prev ele will be greater
# edge case: if both side are sorted 
def minimal_rotated(lst):
    l = 0
    r = len(lst)-1
    while(l<=r):
        m = (l+r)//2
        if lst[m-1]> lst[m]:
            return lst[m]
        if lst[l] > lst[m]:
            r = m-1
        elif lst[m] > lst[r]:
            l = m+1
        else:
            return lst[l]
    return -1

print(minimal_rotated([2,3,4,5,1]))
        