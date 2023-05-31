def can_place_flowers(flowerbed, n):
    count = 0  
    for i in range(len(flowerbed)):  
        if (
            flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):  
            flowerbed[i] = 1 
            count += 1  

        if count >= n:  
            return True

    return False  


flowerbed = [1, 0, 0, 0, 1]
n = 1
can_plant = can_place_flowers(flowerbed, n)
print(can_plant)  