import re

def text_match_two_three(text):
    # Define the regular expression pattern
    pattern = r'a(b{2,3})'
    # Search the pattern in the given text
    match = re.search(pattern, text)
    # Return True if the pattern is found, otherwise False
    return bool(match)

# Test cases
assert text_match_two_three("ac") == False
assert text_match_two_three("dc") == False
assert text_match_two_three("abbbba") == True
