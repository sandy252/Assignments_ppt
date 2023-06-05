def arrangeCoins(n):
    k = 1
    while (k * (k + 1)) // 2 <= n:
        k += 1

    return k - 1

n = 8
result = arrangeCoins(n)
print(result)  