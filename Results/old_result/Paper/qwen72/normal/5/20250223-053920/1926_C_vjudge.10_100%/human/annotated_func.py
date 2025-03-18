#State of the program right berfore the function call: The function should accept an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: `t` remains the same input integer between 1 and 10^4, `inf` remains 200001, `values` is a list where each element at index `i` (for 1 ≤ i < 200001) is the cumulative sum of the digit sums of all integers from 1 to `i`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` remains the same input integer between 1 and 10^4, `inf` remains 200001, `values` remains the same list where each element at index `i` (for 1 ≤ i < 200001) is the cumulative sum of the digit sums of all integers from 1 to `i`.
#Overall this is what the function does:The function `func_1` accepts an integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it reads an integer `n` (1 ≤ n ≤ 2 · 10^5) and prints the cumulative sum of the digit sums of all integers from 1 to `n`. The function does not return any value. After the function concludes, `t` remains the same input integer, `inf` remains 200001, and `values` is a list where each element at index `i` (for 1 ≤ i < 200001) is the cumulative sum of the digit sums of all integers from 1 to `i`.

