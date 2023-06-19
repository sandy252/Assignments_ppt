def merge_arr(a1,a2):
    for i in a2:
        a1.append(i)
    a1.sort()
    return a1

print(merge_arr([1,2,3],[2,5,6]))