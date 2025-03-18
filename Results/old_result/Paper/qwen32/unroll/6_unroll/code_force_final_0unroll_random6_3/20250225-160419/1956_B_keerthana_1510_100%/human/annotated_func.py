#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: A series of integers, each representing the count of integers that appear more than once in the corresponding input line.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` integers. It outputs the count of integers that appear more than once in the list for each test case.

