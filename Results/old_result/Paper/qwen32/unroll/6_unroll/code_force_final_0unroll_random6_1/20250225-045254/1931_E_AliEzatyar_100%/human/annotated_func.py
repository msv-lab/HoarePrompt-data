#State of the program right berfore the function call: num is a list of test cases, where each test case is a list containing two integers n and m, followed by a list of n integers a_1, a_2, ..., a_n, representing the number of integers in the list, the parameter determining when Sasha wins, and the list of integers given to Anna, respectively. The constraints are 1 <= t <= 10^4, 1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6, and 1 <= a_i <= 10^9 for each integer in the list. The sum of n for all test cases does not exceed 2 * 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: num is a list of test cases, where each test case is a list containing two integers `n` and `m`, followed by a list of `n` integers `a_1, a_2, ..., a_n`; `counter` is 0.
    return counter
    #The program returns 0.
#Overall this is what the function does:The function accepts a parameter `num`, which is a list of test cases. Each test case consists of two integers `n` and `m`, followed by a list of `n` integers. The function always returns 0 regardless of the input values.

