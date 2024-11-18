def all_Characters_Same(s):
    if not s:  # If the string is empty, return True (edge case)
        return True
    first_char = s[0]
    for char in s:
        if char != first_char:
            return False
    return True

# Tests
assert all_Characters_Same("python") == False
assert all_Characters_Same("aaa") == True
assert all_Characters_Same("data") == False
