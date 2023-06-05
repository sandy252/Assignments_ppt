def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col


m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)  
