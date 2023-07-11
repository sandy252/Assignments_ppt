def is_prime(n):
    if n==2 or n ==2:
        return True
    se =  n//2+1
    for i in range(2, se):
        if n%i==0:
            return False
    return True

print(is_prime(19))
