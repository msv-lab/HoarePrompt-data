def find_length(binary_string: str) -> int:
    # Transform the binary string into an array of +1 and -1
    transformed = [1 if char == '0' else -1 for char in binary_string]
    
    # Initialize variables for Kadane's algorithm
    max_diff = float('-inf')
    current_diff = 0
    
    for value in transformed:
        current_diff += value
        if current_diff > max_diff:
            max_diff = current_diff
        if current_diff < 0:
            current_diff = 0
    
    return max_diff

# Tests
assert find_length("11000010001") == 6
assert find_length("10111") == 1
assert find_length("11011101100101") == 2
