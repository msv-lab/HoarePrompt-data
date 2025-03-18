#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 100) represents the number of test cases. For each test case, the list contains an integer n (1 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: freq = {1: 2, 5: 1}
    return sum(v // 4 for v in freq.values())
    #The program returns 0
#Overall this is what the function does:The function accepts a list of integers where the first element indicates the number of test cases. Each test case consists of an integer followed by that many integers representing stick lengths. Despite the input, the function always returns 0.

