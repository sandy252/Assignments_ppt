def last_remaining_number(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * last_remaining_number(n // 2) - 1
    else:
        return 2 * last_remaining_number(n // 2) + 1

print(last_remaining_number(9))