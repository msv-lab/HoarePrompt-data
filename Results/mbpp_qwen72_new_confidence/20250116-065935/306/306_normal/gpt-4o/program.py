import re

def check_str(s):
    # Define the regular expression pattern to check if the string starts with a vowel
    pattern = r'^[aeiouAEIOU]'
    # Use re.match to check if the string matches the pattern
    return re.match(pattern, s) is not None

# Tests
assert check_str("annie")
assert not check_str("dawood")
assert check_str("Else")
