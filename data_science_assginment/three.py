def largest(lst):
    m = lst[0]
    # s = lst.sort()
    s = sorted(lst)
    # for e in lst:
    #     if e>m:
    #         m = e
    # return m
    return lst[-1]

print(largest([1,2,3,4,5]))