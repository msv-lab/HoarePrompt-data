def count_char_position(s: str) -> int:
    count = 0
    s = s.lower()
    
    for i, char in enumerate(s):
        if ord(char) - ord('a') == i:
            count += 1
            
    return count

# Test cases
assert count_char_position("xbcefg") == 2
assert count_char_position("ABcED") == 3
assert count_char_position("AbgdeF") == 5
