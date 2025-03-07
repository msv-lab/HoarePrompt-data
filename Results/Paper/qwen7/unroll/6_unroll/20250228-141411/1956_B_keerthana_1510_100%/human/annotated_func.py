#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and for each test case, the list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and for each test case, the list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice. After executing the loop, the value of t remains unchanged, and for each test case, the output is the count of duplicate integers in the input line.
    #
    #The loop processes every second line starting from the third line of the input file (skipping the first two lines). For each processed line, it calculates the number of duplicate tokens (integers) by comparing the length of the split tokens list with the length of the set of those tokens. The result for each line is printed but does not affect the input state.
#Overall this is what the function does:The function processes an input file containing multiple test cases, each consisting of a line of space-separated integers. It skips the first two lines of the file and then, for every second line starting from the third, calculates and prints the count of duplicate integers. The function does not return any value but modifies the state by printing the counts of duplicates for each relevant line. The input file is expected to have a specific structure with `t` test cases, where `1 ≤ t ≤ 10^4`, and each test case contains `n` integers (`1 ≤ n ≤ 2 ⋅ 10^5`), with each integer from 1 to n appearing at most twice.

