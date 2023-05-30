def m_sort(arr1, arr2):
    for ele in arr2:
        arr1.append(ele)
        arr1.sort()
    return arr1
print(m_sort([1,2,3],[2,5,6]))