# # 20. Implement a function to reverse the order of words in a given sentence.
def reverse_words(string):
    words = string.split()
    rev = words[::-1]
    return " ".join(rev)

print(reverse_words("hello my name is sandeep"))

