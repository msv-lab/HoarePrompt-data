#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in the list at most 2 times.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in the list at most 2 times; after executing the loop, the value of t remains unchanged, and for each test case, the variable tokens is an empty list, and the printed result is 0.
    #
    #This means that after the loop executes all its iterations, the number of test cases (t) remains within the given range, and for each test case, the length of the unique tokens minus the length of the split tokens results in 0 because the tokens list is always empty after processing each line.
#Overall this is what the function does:The function processes standard input containing multiple test cases. For each test case, it reads a line, splits the line into tokens, and prints the difference between the number of unique tokens and the total number of tokens. After processing all test cases, the number of test cases remains unchanged, and for each case, the printed result is 0 since the tokens list is always empty after processing.

