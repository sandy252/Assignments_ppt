# 26. Implement a function to find the mode of a list of numbers.
def mode_finder(lst):
    dict = {}
    m = 0
    for e in lst:
        if e in dict:
            dict[e] += 1
            if dict[e]>m:
                m = dict[e]
        else:
            dict[e] = 1
    return m

print(mode_finder([1,2,3,4,5,5]))
            