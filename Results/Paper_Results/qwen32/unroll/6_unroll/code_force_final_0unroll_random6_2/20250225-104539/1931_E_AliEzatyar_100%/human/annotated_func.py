#State of the program right berfore the function call: num is a list of test cases, where each test case is represented as a list containing two integers n and m, followed by a list of n integers a_1, a_2, ..., a_n, with the constraints 1 ≤ t ≤ 10^4, 1 ≤ n ≤ 2 · 10^5, 0 ≤ m ≤ 2 · 10^6, and 1 ≤ a_i ≤ 10^9. The sum of n for all test cases does not exceed 2 · 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: num
    return counter
    #The program returns the value of the variable 'counter'
#Overall this is what the function does:The function `func_1` accepts a parameter `num`, which is expected to be a list. It counts the number of trailing '0' strings from the end of the list and returns this count.

