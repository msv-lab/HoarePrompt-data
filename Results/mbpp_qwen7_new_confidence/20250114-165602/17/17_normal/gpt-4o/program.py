def find_Max_Num(digits):
    # Convert each digit to a string
    str_digits = map(str, digits)
    # Sort the digits in descending order
    sorted_digits = sorted(str_digits, reverse=True)
    # Join the sorted digits to form the largest number
    largest_num_str = ''.join(sorted_digits)
    # Convert the resulting string back to an integer
    return int(largest_num_str)

# Test cases
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,1]) == 6541
assert find_Max_Num([1,2,3,9]) == 9321
