def odd_Equivalent(binary_str, num_rotations):
    count = 0
    for _ in range(num_rotations):
        # Rotate the string by moving the last character to the front
        binary_str = binary_str[-1] + binary_str[:-1]
        # Convert the rotated binary string to an integer
        integer_value = int(binary_str, 2)
        # Check if the integer is odd
        if integer_value % 2 == 1:
            count += 1
    return count

# Testing the function with the provided test cases
assert odd_Equivalent("011001", 6) == 3
assert odd_Equivalent("11011", 5) == 4
assert odd_Equivalent("1010", 4) == 2
