def len_log(words):
    return max(len(word) for word in words)

# Test cases
assert len_log(["python", "PHP", "bigdata"]) == 7
assert len_log(["a", "ab", "abc"]) == 3
assert len_log(["small", "big", "tall"]) == 5
