def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

s = "Let's reverse the words in this sentence."
print(reverseWords(s))
