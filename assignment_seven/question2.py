# # def sumofdigits(n):
# #     if n==0:
# #         return 0
# #     if n ==1:
# #         return 1
# #     return n%10 + sumofdigits(n//10)

# # print(sumofdigits(96))

# def st(s):
#     st_nos = [0,1,8,9,6]
#     d = {}
#     for n in st_nos:
#         if n == 0:
#             d[n] = 0
#         elif n == 1:
#             d[n] = 1
#         elif n == 8:
#             d[n]=8
#         elif n == 9:
#             d[n] = 6
#         elif n == 6:
#             d[n] = 9
#     for digit in s:
#         if int(digit) not in d:
#             return False
#     l = []
#     for i in range(len(s)):
#         l.append(d[int(s[i])])
#     print(l)
#     # if s == ''.join(l):
#     #     return True
#     # else:
#     #     return False
    
# psrint(st('69'))
def st(s):
    st_nos = [0,1,8,9,6]
    d = {}
    for n in st_nos:
        if n == 0:
            d[n] = 0
        elif n == 1:
            d[n] = 1
        elif n == 8:
            d[n]=8
        elif n == 9:
            d[n] = 6
        elif n == 6:
            d[n] = 9
    i = 0
    j = len(s)
    while i<j:
        c = s[i]
        e = s[j-1]
        if int(c) not in d:
            return False
        if d[int(c)] != int(e):
            return False
        i +=1
        j -= 1
    return True

print(st('619'))
