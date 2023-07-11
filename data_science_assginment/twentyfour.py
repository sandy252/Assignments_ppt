#  24. Implement a function to check if a given number is a power of two.
def power_of(n):
    val = n & n-1
    if val == 0:
        return True
    else:
        return False
    

print(power_of(17))