arr1 = [1,2,1,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
# m = max(len(arr1),len(arr2),len(arr3))
def find_c(l1,l2,l3):
    l=[]
    for e in l1:
        if e in arr2 and e in arr3:
            l.append(e)
    l.sort()
    return l

print(find_c(arr1,arr2,arr3))