def is_power_of_three(n):
    if n == 1:
        return True
    elif n <= 0 or n % 3 != 0:
        return False
    else:
        return is_power_of_three(n // 3)

print(is_power_of_three(27))