import re

def is_decimal(s: str) -> bool:
    # Regex pattern to match a number with exactly two decimal places
    pattern = r'^\d+\.\d{2}$'
    return bool(re.match(pattern, s))

# Testing the provided test cases
assert is_decimal('123.11') == True
assert is_decimal('e666.86') == False
assert is_decimal('3.124587') == False
assert is_decimal('1.11') == True
assert is_decimal('1.1.11') == False
