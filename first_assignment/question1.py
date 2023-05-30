arr = [3,2,2,5,7,9,3]
val = 3
for i in arr:
    if i == val:
        arr.remove(i)
print(len(arr))