def digit_distance_nums(num1, num2):
    # Convert numbers to strings
    str1, str2 = str(num1), str(num2)
    
    # Pad the shorter string with leading zeros
    max_len = max(len(str1), len(str2))
    str1, str2 = str1.zfill(max_len), str2.zfill(max_len)
    
    # Calculate the sum of absolute differences of corresponding digits
    total_diff = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str1, str2))
    
    return total_diff

# Provided test cases
assert digit_distance_nums(1, 2) == 1
assert digit_distance_nums(23, 56) == 6
assert digit_distance_nums(123, 256) == 7
