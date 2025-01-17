def first_non_repeating_character(s: str):
    # Dictionary to store the frequency of each character
    char_count = {}
    
    # First pass: count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Second pass: find the first character with a frequency of one
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no such character exists, return None
    return None

# Test cases
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("ababc") == "c"
