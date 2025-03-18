def func_1(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum((int(digit) ** num_len for digit in num_str))
    return armstrong_sum == n
assert func_1(153) == True
assert func_1(259) == False
assert func_1(4458) == False