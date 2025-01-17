def replace_char(s: str, old: str, new: str) -> str:
    return s.replace(old, new)

# Test cases
assert replace_char("polygon", 'y', 'l') == "pollgon"
assert replace_char("character", 'c', 'a') == "aharaater"
assert replace_char("python", 'l', 'a') == "python"
