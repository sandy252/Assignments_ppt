def findNthTerm(a, d, N):
    nthTerm = a + (N - 1) * d
    return nthTerm

a = 3
d = 4
N = 6
nthTerm = findNthTerm(a, d, N)
print(nthTerm)
