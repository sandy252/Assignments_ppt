from collections import Counter

def findAnagrams(s, p):
    result = []
    len_s, len_p = len(s), len(p)

    freq_p = Counter(p)
    freq_window = Counter(s[:len_p])

    if freq_p == freq_window:
        result.append(0)

    for i in range(len_p, len_s):
        if freq_window[s[i - len_p]] == 1:
            del freq_window[s[i - len_p]]
        else:
            freq_window[s[i - len_p]] -= 1

        freq_window[s[i]] += 1

        if freq_p == freq_window:
            result.append(i - len_p + 1)

    return result


s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
print(indices)