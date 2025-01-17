def sum_of_digits(lst):
    total_sum = 0
    for item in lst:
        if isinstance(item, (int, float)):
            total_sum += sum(int(digit) for digit in str(abs(int(item))))
    return total_sum
