#State of the program right berfore the function call: num is an integer representing the number of test cases, where 1 ≤ num ≤ 10^4. Each test case consists of two integers n and m, where 1 ≤ n ≤ 2 × 10^5 and 0 ≤ m ≤ 2 × 10^6, and a list of n integers a_1, a_2, ..., a_n, where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 × 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `counter` is the number of trailing zeros in the list of integers for the last test case, and `num` remains unchanged.
    return counter
    #The program returns the number of trailing zeros in the list of integers for the last test case.
#Overall this is what the function does:The function `func_1` accepts a list of integers and returns the number of trailing zeros in the list. The input list remains unchanged.

