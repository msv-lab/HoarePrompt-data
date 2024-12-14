def is_undulating(n):
    s = str(n)
    if len(s) < 3:
        return False
    first_digit = s[0]
    second_digit = s[1]
    if first_digit == second_digit:
        return False
    
    for i in range(2, len(s)):
        if i % 2 == 0 and s[i] != first_digit:
            return False
        if i % 2 == 1 and s[i] != second_digit:
            return False
            
    return True

# Test cases
assert is_undulating(1212121) == True
assert is_undulating(1991) == False
assert is_undulating(121) == True
