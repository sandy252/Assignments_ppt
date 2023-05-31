def max_candies(candyType):
    unique_candies = set()  
    for candy in candyType:  
        unique_candies.add(candy)  

    return min(len(unique_candies), len(candyType) // 2)  


candyType = [1, 1, 2, 2, 3, 3]
max_types = max_candies(candyType)
print(max_types)  





