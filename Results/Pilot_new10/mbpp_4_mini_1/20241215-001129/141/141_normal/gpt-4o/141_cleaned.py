def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
    return True
assert func_1(1234) == True
assert func_1(51241) == False
assert func_1(321) == True