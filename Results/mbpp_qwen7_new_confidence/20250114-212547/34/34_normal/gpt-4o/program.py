def is_Diff(n):
    # Convert the number to a string to easily access the digits
    n_str = str(n)
    
    # Initialize sums for odd and even positioned digits
    odd_sum = 0
    even_sum = 0
    
    # Iterate through the digits
    for i, digit in enumerate(n_str):
        if i % 2 == 0:  # 0-based index, so 0, 2, 4,... are odd positions
            odd_sum += int(digit)
        else:  # 1, 3, 5,... are even positions
            even_sum += int(digit)
    
    # Calculate the difference between the sums
    diff = abs(odd_sum - even_sum)
    
    # Check if the difference is divisible by 11
    return diff % 11 == 0

# Test cases
assert is_Diff(12345) == False
assert is_Diff(1212112) == True
assert is_Diff(1212) == False
