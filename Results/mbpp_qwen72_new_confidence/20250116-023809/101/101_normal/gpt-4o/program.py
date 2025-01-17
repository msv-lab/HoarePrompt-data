def replace_blank(input_string, replacement_char):
    return input_string.replace(' ', replacement_char)

# Test cases
assert replace_blank("hello people", '@') == "hello@people"
assert replace_blank("python program language", '$') == "python$program$language"
assert replace_blank("blank space", "-") == "blank-space"
