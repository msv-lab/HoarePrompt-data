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
        
    #State: Output State: The final state of the `values` list will be such that each index `i` from 1 to 200000 will hold the sum of the digit sums from 1 to `i`. In other words, `values[i]` will store the cumulative sum of the digit sums of all integers from 1 to `i`.
    #
    #To explain further, for each integer `i` from 1 to 200000, the loop calculates the sum of its digits (`sum_value_digits`) and updates `values[i]` to be the previous value of `values[i-1]` plus `sum_value_digits`. This process continues until the loop has iterated through all possible values up to 200000. Thus, `values[i]` accumulates the total sum of the digit sums from 1 to `i` for every `i` in the range from 1 to 200000.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: Output State: The final state of the `values` list will contain 200,000 elements where each element `values[i]` (for `i` ranging from 0 to 199,999) holds the sum of the digit sums from 1 to `i+1`. In other words, `values[i]` will store the cumulative sum of the digit sums of all integers from 1 to `i+1` for every `i` in the range from 0 to 199,999.
    #
    #This means that after all iterations of the loop, the `values` list will be fully populated with the required sums, starting from `values[0]` which will be the digit sum of 1, and ending with `values[199999]` which will be the sum of the digit sums from 1 to 200,000.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (1 ≤ t ≤ 10^4) and then reads `t` integers `n` (1 ≤ n ≤ 2 · 10^5). It calculates the sum of the digit sums from 1 to each `n` and stores these sums in a list `values`. Finally, it prints the sum of the digit sums for each `n` from the precomputed `values` list.

