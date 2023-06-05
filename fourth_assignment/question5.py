def arrangeCoins(n):
    row = 1
    while n >= row:
        n -= row
        row += 1

    return row - 1


n = 5
result = arrangeCoins(n)
print(result)  # Output: 3




