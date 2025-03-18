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
        
    #State: Output State: `t` is an input integer, `n` is an integer such that 1 ≤ n ≤ 2 * 10^5, `inf` is 200001, `values` is a list where each index `i` (from 1 to 200000) contains the cumulative sum of the digit sums from 1 to `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: `values` is a list where each index `i` (from 1 to 200000) contains the cumulative sum of the digit sums from 1 to `i`, `t` is an input integer, and for each iteration, `value` is set to an integer read from input and then the corresponding cumulative sum from the `values` list is printed. The variable `n` remains unchanged and is not affected by the loop.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digit sums from 1 to `n`. The function initializes a list `values` to store these cumulative sums up to 200,000. After processing all test cases, it does not return any value but prints the required cumulative sums for each test case.

