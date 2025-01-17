def is_Sum_Of_Powers_Of_Two(n):
    bin_str = bin(n)[2:]  # convert the number to binary and remove the '0b' prefix
    return '11' not in bin_str  # check if there are no consecutive 1s in the binary representation