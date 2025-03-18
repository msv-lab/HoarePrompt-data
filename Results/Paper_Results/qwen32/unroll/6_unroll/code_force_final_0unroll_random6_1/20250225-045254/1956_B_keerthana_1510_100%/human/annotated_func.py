#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The following line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: a series of integers, each representing the count of integers that appear more than once in each sequence of integers from the input.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a sequence of integers. It calculates and prints the count of integers that appear more than once in each sequence.

