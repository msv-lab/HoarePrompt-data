#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and the integers a_1, a_2, ..., a_n are a sequence of integers where each integer from 1 through n appears at most twice. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The output state after the loop executes all iterations is the sum of the differences between the length of each line split by spaces and the length of the set of those tokens, for every other line starting from the third line of the input.
#Overall this is what the function does:The function processes a series of test cases from standard input. For each test case, it reads a line, splits the line into tokens, calculates the difference between the number of tokens and the number of unique tokens, and prints this difference. The function does not return any value but produces output for each test case.

