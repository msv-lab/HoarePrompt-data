#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and for each test case, a list of integers a_1, a_2, ..., a_n is given where 1 ≤ a_i ≤ n and each integer from 1 through n appears at most twice in the list.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and for each test case, a list of integers a_1, a_2, ..., a_n is given where 1 ≤ a_i ≤ n and each integer from 1 through n appears at most twice in the list. After executing the loop, for each test case, the variable `result` holds the number of duplicate tokens in each line of input, where duplicates are counted based on the number of occurrences minus the number of unique tokens.
    #
    #In simpler terms, for each test case, the loop processes every second line starting from the third line of input (skipping the first two lines). It calculates how many tokens are repeated in each line by comparing the length of the split tokens with the length of the set of those tokens. The result for each line is printed but not stored elsewhere, so the final state retains the original lists of integers without any changes.
#Overall this is what the function does:The function processes a series of test cases, each containing a list of integers. It skips the first two lines of input and then for every subsequent even-indexed line, it calculates the number of duplicate integers by comparing the count of unique integers with the total count of integers in that line. The result for each line is printed but not stored elsewhere. The final state of the program retains the original lists of integers without any changes.

