#State of the program right berfore the function call: The function should take two parameters: t (1 \leq t \leq 10^4) representing the number of test cases, and a list of integers n (1 \leq n \leq 2 \cdot 10^5) for each test case, where n is the largest number written on the board.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: `t` remains unchanged, `inf` remains 200001, `values` is a list where each element at index `i` (for `i` from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`, and `n` remains a list of integers where each integer is between 1 and 200000.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: `t` remains unchanged, `inf` remains 200001, `values` remains a list where each element at index `i` (for `i` from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`, and `n` remains a list of integers where each integer is between 1 and 200000. The loop prints the cumulative sum of the digits of all integers from 1 to the value provided by the user for each iteration of the loop.
#Overall this is what the function does:The function `func_1` does not accept any parameters and does not return any values. It reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads another integer from the user input, calculates the cumulative sum of the digits of all integers from 1 to that number, and prints the result. After processing all test cases, the function ends with `t` remaining unchanged, and `values` being a list where each element at index `i` (for `i` from 1 to 200000) contains the cumulative sum of the digits of all integers from 1 to `i`.

