def matrix_t(mat):
    ma = [[0] * len(mat) for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            ma[j][i] = mat[i][j]           
    return ma

print(matrix_t([[1,2,3],[4,5,6],[7,8,9]]))