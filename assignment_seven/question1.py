def isIsomorphic(s, t):
    mst, mts = {}, {}
    for i in range(len(s)):
        if ((s[i] in mst and mst[s[i]] != t[i]) or (t[i] in mts and mts[t[i]] != s[i])):
            return False
        mst[s[i]] = t[i]
        mts[t[i]] = s[i]
    return True

print(isIsomorphic('foo', "bar"))