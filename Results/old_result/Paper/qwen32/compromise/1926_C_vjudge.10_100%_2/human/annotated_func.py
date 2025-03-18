#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 ⋅ 10^5) representing the largest number Vladislav writes for each test case.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` is an input integer representing the number of test cases, `inf` is 200001, `values` is a list of 200001 zeros except `values[200000]` which is `t` plus the cumulative sum of the digits of all numbers from `1` to `200000`.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` is the initial number of test cases, `inf` is 200001, `values` is a list of 200001 zeros except `values[200000]` which is `t` plus the cumulative sum of the digits of all numbers from `1` to `200000`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digits of all numbers from 1 to `n`.

