def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            temp = 0
            for x in range(k):
                temp += mat1[i][x] * mat2[x][j]
            result[i][j] = temp

    return result


print(multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]]))