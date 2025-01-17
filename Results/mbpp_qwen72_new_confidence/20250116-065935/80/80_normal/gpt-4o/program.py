def is_Sum_Of_Powers_Of_Two(n):
    # Convert the number to binary and check if all digits are either 0 or 1
    # bin(n) gives the binary representation in '0b...' format, so we strip off the '0b'.
    binary_representation = bin(n)[2:]
    
    # Check if all characters in the binary representation are '0' or '1'
    for digit in binary_representation:
        if digit != '0' and digit != '1':
            return False
    return True

# Test cases
assert is_Sum_Of_Powers_Of_Two(10) == True  # 10 = 2^1 + 2^3
assert is_Sum_Of_Powers_Of_Two(7) == False  # 7 = 2^0 + 2^1 + 2^2 (but all powers used are non-zero)
assert is_Sum_Of_Powers_Of_Two(14) == True  # 14 = 2^1 + 2^2 + 2^3
