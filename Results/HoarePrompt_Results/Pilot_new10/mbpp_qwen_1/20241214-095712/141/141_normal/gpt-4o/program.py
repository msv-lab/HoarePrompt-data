def validate(n):
    digit_str = str(n)
    frequency = {}
    
    # Calculate frequency of each digit
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    
    # Check the condition for each digit
    for digit, count in frequency.items():
        if count > int(digit):
            return False
    
    return True

# Tests
assert validate(1234) == True
assert validate(51241) == False
assert validate(321) == True
