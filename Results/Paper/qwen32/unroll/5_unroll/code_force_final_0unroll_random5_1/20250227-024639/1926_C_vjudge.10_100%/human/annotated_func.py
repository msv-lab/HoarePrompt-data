#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes for each test case.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is an input integer representing the number of test cases. Each of the next `t` lines contains a single integer `n` (1 ≤ `n` ≤ 2 · 10^5) representing the largest number Vladislav writes for each test case; `inf` is 200001; `values` is a list where the first 200001 elements contain the cumulative sum of the digit sums from 1 to the respective index, and the rest are 0.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` is an input integer representing the number of test cases. Each of the next `t` lines contains a single integer `n` (1 ≤ `n` ≤ 2 · 10^5) representing the largest number Vladislav writes for each test case; `inf` is 200001; `values` is a list where the first 200001 elements contain the cumulative sum of the digit sums from 1 to the respective index, and the rest are 0. The loop has printed the cumulative sum of the digit sums for each `n` provided in the input.
#Overall this is what the function does:The function `func_1` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digit sums from 1 to `n`.

