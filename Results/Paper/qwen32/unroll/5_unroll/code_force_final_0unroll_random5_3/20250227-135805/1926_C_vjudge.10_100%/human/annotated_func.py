#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: The input consists of an integer `t` (1 ≤ `t` ≤ 10^4) representing the number of test cases; `inf` is 200001; `values` is a list where `values[0]` is 0 and `values[i]` for i from 1 to 200000 is the cumulative sum of the digit sums of all numbers from 1 to i.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The `values` list remains unchanged with `values[0]` as 0 and `values[i]` for `i` from 1 to 200000 as the cumulative sum of the digit sums of all numbers from 1 to `i`. The constant `inf` remains 200001.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digit sums of all numbers from 1 to `n`.

