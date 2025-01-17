def remove_whitespaces(s: str) -> str:
    return ''.join(s.split())

# Test cases to ensure the function works as expected
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
