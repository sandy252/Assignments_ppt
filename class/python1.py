arr = [7,1,5,3,6,4]



# def max_profit(arr):
#     max = 0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             profit = arr[j] - arr[i]
#             if profit > max:
#                 max = profit
#     return max

# print(max_profit(arr))
def max_profit(arr):
    max_profit = 0
    min = 1000
    for i in range(len(arr)):
        price = arr[i]
        if min > price:
            min = price
        elif arr[i]-min > max_profit:
            max_profit = arr[i]-min 
    return max_profit

print(max_profit(arr))
                