#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 10^4) as the number of test cases, and for each test case, an integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes.
def func_1():
    inf = 2 * 10 ** 5 + 1
    t = int(input())
    values = [0] * inf
    for i in range(1, inf):
        sum_value_digits = 0
        
        for x in str(i):
            sum_value_digits += int(x)
        
        values[i] = values[i - 1] + sum_value_digits
        
    #State: Output State: `t` remains the input integer provided by the user, `inf` is 200001, `values` is a list where each element at index `i` (for `i` from 1 to 200000) is the sum of the digits of all integers from 1 to `i` added to the previous element in the list.
    for _ in range(t):
        value = int(input())
        
        print(values[value])
        
    #State: The value of `t` remains unchanged as the input integer provided by the user, `inf` remains 200001, and `values` remains the same list where each element at index `i` (for `i` from 1 to 200000) is the sum of the digits of all integers from 1 to `i` added to the previous element in the list. The loop prints the sum of the digits of all integers from 1 to the user-provided `value` for each iteration, but does not modify any of the variables in the loop head or body.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the user, representing the number of test cases (1 ≤ t ≤ 10^4). For each test case, it reads another integer `n` (1 ≤ n ≤ 2 · 10^5) and prints the sum of the digits of all integers from 1 to `n`. The function does not return any value but prints the result for each test case. After the function concludes, the value of `t` remains unchanged, and the list `values` contains the cumulative sum of the digits of all integers from 1 to 200000.

