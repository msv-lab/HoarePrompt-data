def word_len(word):
    return len(word) % 2 != 0

# Tests
assert word_len("Hadoop") == False
assert word_len("great") == True
assert word_len("structure") == True
