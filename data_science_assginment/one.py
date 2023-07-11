# def reverse(str):
#     return (str[::-1])


def reveres(str):
    rev = ""
    for i in range(len(str)):
        rev = str[i]+rev
    return rev
        

print(reveres("sandeep"))