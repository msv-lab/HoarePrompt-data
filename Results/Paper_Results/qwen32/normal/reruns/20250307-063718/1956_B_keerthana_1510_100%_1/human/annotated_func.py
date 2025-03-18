#State of the program right berfore the function call: There are multiple test cases, where each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The output consists of the differences between the number of tokens and the number of unique tokens for each line processed by the loop, which are every second line starting from the third line of the input file.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a list of integers. It then calculates and prints the number of integers that appear exactly once in each list.

