#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: `t` is an input integer, 1 ≤ `t` ≤ 10^4, `n` is an integer such that 1 ≤ `n` ≤ 2 * 10^5, `inf` is 200001, `values` is a list where each index `i` (1 ≤ `i` ≤ 200000) contains the sum of the digits of all integers from 1 to `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: `t` is an input integer, 1 ≤ `t` ≤ 10^4, `n` is an integer such that 1 ≤ `n` ≤ 2 * 10^5, `inf` is 200001, `values` is a list where each index `i` (1 ≤ `i` ≤ 200000) contains the sum of the digits of all integers from 1 to `i`, for each iteration `_` in range `t`, the code reads an integer `value` from input, then prints the corresponding element in the `values` list.
#Overall this is what the function does:The function processes an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 2·10^5) and prints the sum of the digits of all integers from 1 to `n`. The function does not return any value but prints the results directly.

