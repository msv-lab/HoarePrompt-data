import re

def text_lowercase_underscore(input_string):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')
    return bool(pattern.match(input_string))

# Tests
assert text_lowercase_underscore("aab_cbbbc") == True
assert text_lowercase_underscore("aab_Abbbc") == False
assert text_lowercase_underscore("Aaab_abbbc") == False
