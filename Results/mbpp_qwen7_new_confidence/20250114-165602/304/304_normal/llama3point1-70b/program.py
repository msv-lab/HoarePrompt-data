def toggle_middle_bits(n):
    # Convert the number to binary and remove the '0b' prefix
    bin_n = bin(n)[2:]
    
    # Toggle the middle bits by XORing with a string of 1s
    toggled_bin = bin_n[0] + ''.join('1' if bit == '0' else '0' for bit in bin_n[1:-1]) + bin_n[-1]
    
    # Convert the toggled binary string back to an integer
    toggled_n = int(toggled_bin, 2)
    
    return toggled_n
