#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: Number of duplicate integers in the list provided for the single test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of integers. It calculates and prints the number of duplicate integers in each list.

