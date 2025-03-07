#State of the program right berfore the function call: num is a list of test cases, where each test case is represented as a list containing an integer t (1 ≤ t ≤ 10^4) followed by t pairs of lists. Each pair consists of a list with two integers [n, m] (1 ≤ n ≤ 2 · 10^5, 0 ≤ m ≤ 2 · 10^6) and a list of n integers [a_1, a_2, ..., a_n] (1 ≤ a_i ≤ 10^9). The sum of n across all test cases does not exceed 2 · 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is a list of test cases, `counter` is the number of consecutive '0' elements from the end of the list until a non-'0' element is encountered or the list is exhausted.
    return counter
    #The program returns `counter`, which is the number of consecutive '0' elements from the end of the list `num` until a non-'0' element is encountered or the list is exhausted.
#Overall this is what the function does:The function accepts a list `num` and returns the count of consecutive '0' elements from the end of the list until a non-'0' element is encountered or the list is exhausted.

