def is_anagram(s, t):
    if len(s) != len(t):
        return False
    dit= {}
    dict = {}
    s = list(s)
    t = list(t)
    for a, b in zip(s, t):
        if a not in dit:
            dit[a] = 1
        else:
            dit[a] += 1
        if b not in dict:
            dict[b] = 1
        else:
            dict[b] += 1
    if dit == dict:
        return True
    else:
        return False





    # s = list(s)
    # t = list(t)
    # s.sort()
    # t.sort()
    # if s != t:
    #     return False
    # else:
    #     return True

print(is_anagram("listens", "silents"))