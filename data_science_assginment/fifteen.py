# 15. Write a program to find the median of a list of numbers.
def median(lst):
    # s = lst.sort()
    l = len(lst)
    median = (l+1)/2
    return median

lst = [1,23,4,9]
print(median(lst))
# print(sorted(lst))