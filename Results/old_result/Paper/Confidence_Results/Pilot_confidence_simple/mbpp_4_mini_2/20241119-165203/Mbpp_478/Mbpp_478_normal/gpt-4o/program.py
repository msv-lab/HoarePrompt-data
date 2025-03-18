def remove_lowercase(s: str) -> str:
    return ''.join([char for char in s if char.isupper()])

# Testing the function
assert remove_lowercase("PYTHon") == 'PYTH'
assert remove_lowercase("FInD") == 'FID'
assert remove_lowercase("STRinG") == 'STRG'
