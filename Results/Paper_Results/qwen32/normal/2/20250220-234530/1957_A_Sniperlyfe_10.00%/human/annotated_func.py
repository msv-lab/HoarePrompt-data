#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 100) represents the number of test cases, followed by pairs of elements where the first element of each pair n (1 ≤ n ≤ 100) represents the number of sticks in the corresponding test case, and the next n elements are integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
def func_1(arr):
    freq = {}
    for n in arr:
        freq[n] = freq.get(n, 0) + 1
        
    #State: arr is a list of integers where the first element t (1 ≤ t ≤ 100) represents the number of test cases, followed by pairs of elements where the first element of each pair n (1 ≤ n ≤ 100) represents the number of sticks in the corresponding test case, and the next n elements are integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks; freq is a dictionary with keys as the unique values of n encountered and their values as the count of how many times each n appeared.
    return sum(v // 4 for v in freq.values())
    #The program returns the sum of the integer divisions of the counts of each unique number of sticks by 4.
#Overall this is what the function does:The function processes a list of integers where the first element indicates the number of test cases. Each test case starts with an integer representing the number of sticks, followed by the lengths of those sticks. The function calculates and returns the sum of the integer divisions of the counts of each unique number of sticks by 4.

