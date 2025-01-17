def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(num):
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
    
    result = []
    for num in range(startnum, endnum + 1):
        if is_divisible_by_digits(num):
            result.append(num)
    
    return result

# Test cases
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(1, 15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
assert divisible_by_digits(20, 25) == [22, 24]
