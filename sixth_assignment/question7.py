def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    current_number = 1

    while current_number <= n**2:
        for col in range(col_start, col_end + 1):
            matrix[row_start][col] = current_number
            current_number += 1
        row_start += 1

        for row in range(row_start, row_end + 1):
            matrix[row][col_end] = current_number
            current_number += 1
        col_end -= 1

        if row_start <= row_end:
            for col in range(col_end, col_start - 1, -1):
                matrix[row_end][col] = current_number
                current_number += 1
            row_end -= 1

        if col_start <= col_end:
            for row in range(row_end, row_start - 1, -1):
                matrix[row][col_start] = current_number
                current_number += 1
            col_start += 1

    return matrix

print(generateMatrix(3))