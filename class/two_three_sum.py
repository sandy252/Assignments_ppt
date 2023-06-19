# arr = [-5,-4,2,3,9]
arr = [-1,0,1,2,-1,-4]

# arr = [-1,0,1,2,-1,-4]
#  arr = [-4,-1,-1,0,1,2]


def three_sum(arr):
    l = []
    x = sorted(arr)
    print(x)
    for i in range(len(x)-2):
        left = i+1
        right = len(x)-1
        while(left< right):
            s = x[i]+x[left]+x[right]
            if s == 0:
                l.append([x[i],x[left],x[right]])
                left+=1
                right-=1
                # print(l)
            if s < 0:
                left+=1
            else:
                right-=1
    return l

print(three_sum(arr))
        

        



# def two_sum_problem(arr):
#     sum = 5
#     l = 0
#     r = len(arr)-1
#     lst= []
#     for i in range(len(arr)):
#         s = arr[l] + arr[r]
#         if s == sum:
#             lst.append([arr[l],arr[r]])
#             l+=1
#         elif s < sum:
#             l += 1
#         elif s>sum:
#             r -=1
#     return lst

# print(two_sum_problem(arr))

# arr = [1,2,5,-2,-1]
# print(arr.sort())