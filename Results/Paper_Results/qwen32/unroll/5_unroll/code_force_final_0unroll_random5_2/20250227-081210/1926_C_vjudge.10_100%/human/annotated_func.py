#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes for that test case.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: the `values` list will have each index `i` containing the cumulative sum of the digit sums from 1 to `i`, and `t` and `n` remain unchanged.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: - Since the `values` list and the variables `t` and `n` are not modified by the loop, they remain in their initial state.
    #   - The loop prints values from the `values` list based on the input provided, but this does not change the state of the variables.
    #
    #Thus, the output state is the same as the initial state, with the `values` list and the variables `t` and `n` unchanged.
    #
    #Output State:
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digit sums from 1 to `n`.

