def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Test cases
assert reverse_words("python program") == "program python"
assert reverse_words("java language") == "language java"
assert reverse_words("indian man") == "man indian"
