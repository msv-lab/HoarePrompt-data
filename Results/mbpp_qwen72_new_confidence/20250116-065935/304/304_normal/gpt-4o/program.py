def toggle_middle_bits(num):
    # Convert the number to its binary representation as a string
    bin_str = bin(num)[2:]
    
    # If the number has less than 3 bits, there are no middle bits to toggle
    if len(bin_str) <= 2:
        return num
    
    # Extract the first and last bits
    first_bit = bin_str[0]
    last_bit = bin_str[-1]
    
    # Toggle the middle bits
    middle_bits = ''.join('1' if bit == '0' else '0' for bit in bin_str[1:-1])
    
    # Combine the first bit, toggled middle bits, and last bit
    toggled_bin_str = first_bit + middle_bits + last_bit
    
    # Convert the binary string back to an integer
    return int(toggled_bin_str, 2)

# Test cases
assert toggle_middle_bits(9) == 15
assert toggle_middle_bits(10) == 12
assert toggle_middle_bits(11) == 13
assert toggle_middle_bits(0b1000001) == 0b1111111
assert toggle_middle_bits(0b1001101) == 0b1110011
