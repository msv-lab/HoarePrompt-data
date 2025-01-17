def power_base_sum(base, power):
    # Calculate the base raised to the given power
    result = base ** power
    
    # Convert the result to a string to iterate over each digit
    result_str = str(result)
    
    # Sum the digits of the resulting string
    digit_sum = sum(int(digit) for digit in result_str)
    
    return digit_sum

# Test cases
assert power_base_sum(2, 100) == 115
assert power_base_sum(8, 10) == 37
assert power_base_sum(8, 15) == 62
assert power_base_sum(3, 3) == 9
