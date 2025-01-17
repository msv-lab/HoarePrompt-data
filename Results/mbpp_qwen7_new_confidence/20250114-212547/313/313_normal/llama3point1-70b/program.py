def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        digits = [int(d) for d in str(num)]
        if all(num % digit == 0 for digit in digits if digit != 0):
            result.append(num)
    return result
