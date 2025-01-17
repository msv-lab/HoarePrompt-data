import re

def text_match_three(text):
    pattern = r'a[b]{3}'
    match = re.search(pattern, text)
    return bool(match)

# Test cases
assert not text_match_three("ac")
assert not text_match_three("dc")
assert text_match_three("abbbba")
assert text_match_three("caacabbbba")
