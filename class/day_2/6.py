def mark_multiples(a, b):
    mul = []
    for i in range(a, b+1):
        if i%2==0 or i%5 == 0:
            mul.append(i)
    return mul

print(mark_multiples(2,10))
