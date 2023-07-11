#  27. Write a program to find the greatest common divisor (GCD) of two numbers.
def gcd(m,n):
    if n == 0:
        return m
    return gcd(n,m%n)


print(gcd(100,10))