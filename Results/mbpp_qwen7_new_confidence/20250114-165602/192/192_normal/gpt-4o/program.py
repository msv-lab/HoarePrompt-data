def remove_odd(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 != 0])

# Testing the function with the provided test cases
assert remove_odd("python") == "yhn"
assert remove_odd("program") == "rga"
assert remove_odd("language") == "agae"
