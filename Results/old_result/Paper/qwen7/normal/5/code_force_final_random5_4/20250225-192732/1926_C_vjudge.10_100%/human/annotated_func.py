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
        
    #State: Output State: The final state of `values` will be a list where each index `i` (from 0 to 200000) contains the cumulative sum of the digit sums from 1 to `i`. In other words, `values[i]` will hold the sum of the digit sums of all integers from 1 to `i`. This means that for each index `i` in the `values` list, it will store the result of summing the digits of all numbers from 1 up to `i`.
    #
    #For example, `values[1]` will be 1 (since the digit sum of 1 is 1), `values[2]` will be 3 (since the digit sum of 1+2 is 3), `values[3]` will be 6 (since the digit sum of 1+2+3 is 6), and so on, until `values[200000]`, which will be the sum of the digit sums of all numbers from 1 to 200000.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The final state of `values` will contain the cumulative sum of the digit sums from 1 to 200000 for each index from 0 to 200000.
#Overall this is what the function does:The function processes a series of test cases where each test case involves an integer `t` (1 ≤ t ≤ 10^4). For each test case, it reads another integer `value` (1 ≤ value ≤ 2 * 10^5) and prints the cumulative sum of the digit sums from 1 to `value`. The function precomputes and stores the cumulative sums of digit sums in a list `values` of size 200001 before processing any test cases. After processing all test cases, the final state of the program includes the precomputed list `values`.

