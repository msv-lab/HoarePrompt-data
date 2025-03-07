#State of the program right berfore the function call: num is a list of test cases, where each test case is represented as a list containing two integers n and m, followed by a list of n integers a_1, a_2, ..., a_n. Here, 1 <= t <= 10^4 is the number of test cases, 1 <= n <= 2 * 10^5, 0 <= m <= 2 * 10^6, and 1 <= a_i <= 10^9 for each element in the list. The sum of n across all test cases does not exceed 2 * 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` remains unchanged, `counter` is the number of consecutive '0's found at the end of `num` before encountering a non-'0' value.
    return counter
    #The program returns the number of consecutive '0's found at the end of `num` before encountering a non-'0' value.
#Overall this is what the function does:The function accepts a list `num` and returns the number of consecutive zeros found at the end of the list before encountering a non-zero value.

