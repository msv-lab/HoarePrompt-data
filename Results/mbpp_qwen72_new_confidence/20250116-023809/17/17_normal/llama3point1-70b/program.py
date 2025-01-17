def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True))))
