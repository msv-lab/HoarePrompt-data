#State of the program right berfore the function call: The function should accept two parameters: an integer t representing the number of test cases (1 ≤ t ≤ 10^4), and a list of integers n representing the largest number for each test case (1 ≤ n[i] ≤ 2 · 10^5).
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `values` is a list where `values[i]` represents the cumulative sum of the digit sums from 1 to `i` for all `i` in the range 1 to 200000, and `t` and `n` remain unchanged.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The list `values` remains unchanged, and `t` and `n` remain unchanged. The loop prints the cumulative sum of the digit sums from 1 to `value` for each input `value` provided, where `value` is an integer read from the input for each iteration of the loop.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, representing the number of test cases, and then reads `t` integers, each representing a value for a test case. It calculates the cumulative sum of the digit sums from 1 to 200000 and stores these sums in a list `values`. For each test case, it prints the cumulative sum of the digit sums from 1 to the given value. The function does not return any value; it only prints the results. The list `values` and the integer `t` remain unchanged after the function concludes.

