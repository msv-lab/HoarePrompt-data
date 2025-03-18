#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 100) represents the number of test cases. For each test case, the list contains an integer n (1 ≤ n ≤ 100) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the stick lengths.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: `arr` is a list of integers where the first element `t` represents the number of test cases. For each test case, the list contains an integer `n` followed by `n` integers representing the stick lengths; `freq` is a dictionary with keys as the integers from `arr` and values as the counts of how many times each integer appears in `arr`.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer division of each value in the dictionary `freq` by 4.
#Overall this is what the function does:The function takes a list of integers where the first element represents the number of test cases, and each subsequent element describes stick lengths for those test cases. It returns the total count of how many sets of four sticks can be formed from all the stick lengths provided across all test cases.

