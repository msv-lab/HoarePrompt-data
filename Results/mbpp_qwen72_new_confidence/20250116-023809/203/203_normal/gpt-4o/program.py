import re

def text_match_wordz(text):
    # Use regular expression to search for a word containing 'z'
    # \b asserts a position at a word boundary
    # \w* matches zero or more word characters
    # z matches the character 'z'
    pattern = r'\b\w*z\w*\b'
    return bool(re.search(pattern, text))

# Tests
assert text_match_wordz("pythonz.") == True
assert text_match_wordz("xyz.") == True
assert text_match_wordz("  lang  .") == False
