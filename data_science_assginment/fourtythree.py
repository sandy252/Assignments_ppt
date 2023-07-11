def occ(e, lst):
    c = 0
    for ele in lst:
        if e == ele:
            c += 1
    return c

print(occ(1,[1,1,1,2,3,4,12]))