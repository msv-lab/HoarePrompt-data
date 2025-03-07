#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and n is an integer such that 1 <= n <= 2 * 10^5 for each test case.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 2 * 10^5 for each test case, `inf` is 200001, `values` is a list of 200001 integers where `values[i]` is the sum of the sums of the digits of all integers from 1 to `i` inclusive for all `i` from 1 to `inf - 1`, `i` is `inf`, `sum_value_digits` is the sum of the digits of `inf - 1`, `x` is the last digit of `inf - 1`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` is an input integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 2 * 10^5 for each test case, `inf` is 200001, `values` is a list of 200001 integers where `values[i]` is the sum of the sums of the digits of all integers from 1 to `i` inclusive for all `i` from 1 to `inf - 1`, `i` is `inf`, `sum_value_digits` is the sum of the digits of `inf - 1`, `x` is the last digit of `inf - 1`, `_` is `t - 1`.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, where `1 <= t <= 10^4`, representing the number of test cases. For each test case, it reads another integer `n` from the input, where `1 <= n <= 2 * 10^5`. It then prints the sum of the sums of the digits of all integers from 1 to `n` inclusive. After processing all test cases, the function does not return any value, but it has printed the required sums for each test case. The final state of the program includes the variable `t` being the number of test cases, `inf` being 200001, and `values` being a list of 200001 integers where `values[i]` is the sum of the sums of the digits of all integers from 1 to `i` inclusive for all `i` from 1 to `inf - 1`.

