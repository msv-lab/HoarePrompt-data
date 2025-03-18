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
        
    #State: After all iterations of the loop, `i` will be 200001, `sum_value_digits` will be the sum of the digits of `i-1`, and `values[200001]` will be the cumulative sum of `sum_value_digits` for all integers from 1 to 200000.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: After all iterations of the loop have finished, `t` will be 0, and `value` will be an input integer that has never been used within the loop during its execution. The variable `sum_value_digits` will hold the sum of the digits of `200000 - 1`, which is 18 (since 1 + 9 + 8 + 9 + ... + 1 + 9 + 8 + 9 = 18), and `values[200001]` will be the cumulative sum of `sum_value_digits` for all integers from 1 to 200000, which is 18 * 200000 / 2 = 1,800,000.
#Overall this is what the function does:The function processes an integer `t` representing the number of test cases, where each test case involves an integer `n` within the range 1 to 200000. For each test case, it calculates the cumulative sum of the digit sums of all integers from 1 to `n` and prints this value. The function does not return any value.

