
def sq_root(n):
    if n<2:
        return n
    l = 1
    r = n //2
    while(l<=r):
        mid = (l+r)//2
        square = mid * mid
        print(square)
        if square == n:
            return mid
        elif square > n:
            r = mid-1
        else:
            l = mid+1

print(sq_root(17))