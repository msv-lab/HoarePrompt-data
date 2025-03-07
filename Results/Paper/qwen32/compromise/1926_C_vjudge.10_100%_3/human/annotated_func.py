#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is an input integer (1 ≤ `t` ≤ 10^4); `n` is a single integer for each of the next `t` lines (1 ≤ `n` ≤ 2 · 10^5); `inf` is 200001; `values` is a list of 200001 integers where `values[i]` is the sum of the digits of all integers from 1 to `i` for `1 ≤ i ≤ 200000`; `i` is 200001; `sum_value_digits` is the sum of the digits of 200000.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` is an input integer (1 ≤ `t` ≤ 10^4); `value` is the last input integer read; `values`, `inf`, `i`, and `sum_value_digits` remain unchanged.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each of the next `t` lines, it reads an integer `n` and prints the sum of the digits of all integers from 1 to `n`.

