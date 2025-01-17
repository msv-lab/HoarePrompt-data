def is_Diff(n):
    return sum(int(digit) for index, digit in enumerate(str(n)) if index % 2 == 0) - sum(int(digit) for index, digit in enumerate(str(n)) if index % 2 == 1) == 0 or sum(int(digit) for index, digit in enumerate(str(n)) if index % 2 == 0) - sum(int(digit) for index, digit in enumerate(str(n)) if index % 2 == 1) == 11
