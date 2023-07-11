def check_(lst):
    s = sorted(lst)
    if s == lst:
        return True
    else:
        return False
    
print(check_([12,3,4,5]))