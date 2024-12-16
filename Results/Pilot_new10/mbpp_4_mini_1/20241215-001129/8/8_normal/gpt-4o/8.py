def remove_Occ(s: str, ch: str) -> str:
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    
    if first_index == -1 or last_index == -1 or first_index == last_index:
        return s  # No removal needed if ch is not found or only one occurrence
    
    # Create a new string without the first and last occurrence of ch
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]

# Testing the function with the provided test cases
assert remove_Occ("hello", "l") == "heo"
assert remove_Occ("abcda", "a") == "bcd"
assert remove_Occ("PHP", "P") == "H"
