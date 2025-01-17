import re

def text_starta_endb(s: str) -> bool:
    # Define the regex pattern to match the specified condition
    pattern = r'^a.*b$'
    # Use re.match to check if the entire string matches the pattern
    return bool(re.match(pattern, s))

# Testing provided assertions
assert text_starta_endb("aabbbb")
assert not text_starta_endb("aabAbbbc")
assert not text_starta_endb("accddbbjjj")
