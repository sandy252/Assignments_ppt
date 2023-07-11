# 14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.

# def fib(n):
#     seq = []
#     if n >= 0:
#         seq.append(0)
#     if n == 1:
#         seq.append(1)
#     for i in range(2,n):
#         out = fib(n-1) + fib(n-2) 
#         seq.append(out)

#     return seq

# print(fib(5))

def fibonacci(n):
    sequence = []
    
    if n >= 1:
        sequence.append(0)  # First Fibonacci number
    if n >= 2:
        sequence.append(1)  # Second Fibonacci number
    
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    
    return sequence

# Example usage
number = int(input("Enter a number: "))
fib_seq = fibonacci(number)
print(fib_seq)
