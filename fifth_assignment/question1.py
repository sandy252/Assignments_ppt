def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []  

    twoDArray = [[0] * n for _ in range(m)]
    for i in range(len(original)):
        row = i // n
        col = i % n
        twoDArray[row][col] = original[i]

    return twoDArray


original = [1,2,3,4]
m = 2
n = 2
result = construct2DArray(original, m, n)
print(result)
