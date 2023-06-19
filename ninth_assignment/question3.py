def factorial(N):
    factorial = 1

    for i in range(1, N + 1):
        factorial *= i

    return factorial


print(factorial(5))