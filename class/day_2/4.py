arr = [1,2,2,2,4,5,6]


def rep(arr):
    # di = {}
    # n = len(arr)
    # for ele in arr:
    #     if ele not in di.keys():
    #         di[ele] = 1
    #     else:
    #         di[ele] = di[ele]+1
    # # return di
    # for key, value in di.items():
    #     if value > n//2:
    #         return key
    # return -1
    # s = set(arr)
    s=set()
    for ele in arr:
        if ele in s:
            return ele
        s.add(ele)
    return s
       

print(rep(arr))
