def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product


arr = [2, 3, 4, 5]
product = productOfArray(arr)
print(product)