#State of the program right berfore the function call: The function should take two parameters: t (1 \leq t \leq 10^4) representing the number of test cases, and a list of integers n (1 \leq n \leq 2 \cdot 10^5) for each test case.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: `t` remains the same input integer between 1 and 10^4, `inf` is 200001, `values` is a list where each element at index `i` (for `i` from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The value of `t` remains the same input integer between 1 and 10^4, `inf` is 200001, `values` is a list where each element at index `i` (for `i` from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`. The loop prints the cumulative sum of the digits of the integers from 1 to `value` for each input `value` provided `t` times.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any values. It reads an integer `t` from the input, which represents the number of test cases, and ensures `t` is between 1 and \(10^4\). It then precomputes a list `values` where each element at index `i` (from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`. For each of the `t` test cases, it reads an integer `value` from the input, and prints the cumulative sum of the digits of the integers from 1 to `value`. The function does not handle invalid inputs or return error messages. After the function concludes, `t` remains the same input integer, `inf` is 200001, and `values` contains the precomputed cumulative sums.

