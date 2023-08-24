def minimal_signed_binary(n):
    # Convert the binary string to a list of integers
    binary_list = [int(d) for d in str(n)]
    
    # Initialize the signed binary representation with all zeros
    signed_binary = [0] * len(binary_list)
    
    # Iterate through the binary list
    for i in range(len(binary_list)):
        # If the current digit is 1, set the signed binary representation to +1
        if binary_list[i] == 1:
            signed_binary[i] = 1
            # Check if the previous digit is also 1
            if i > 0 and binary_list[i-1] == 1:
                # If so, set the previous digit to 0 since it can be represented as -1
                signed_binary[i-1] = 0
        
        # If the current digit is 0, set the signed binary representation to 0
        elif binary_list[i] == 0:
            signed_binary[i] = 0
        
        # If the current digit is 2, set the signed binary representation to -1
        elif binary_list[i] == 2:
            signed_binary[i] = -1
            # Check if the previous digit is also 1
            if i > 0 and binary_list[i-1] == 1:
                # If so, set the previous digit to 0 since it can be represented as -1
                signed_binary[i-1] = 0
    
    # Convert the signed binary representation to a string
    signed_binary_str = ''.join(['+' if d == 1 else '-' if d == -1 else '0' for d in signed_binary])
    
    return signed_binary_str

# Read the input
n = input()

# Generate the minimal signed binary representation
minimal_rep = minimal_signed_binary(n)

# Print the result
print(minimal_rep)