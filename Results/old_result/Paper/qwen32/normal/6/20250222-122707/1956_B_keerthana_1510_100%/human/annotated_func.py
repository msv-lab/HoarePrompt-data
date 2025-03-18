#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The following line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: A series of printed integers, each representing the difference between the number of tokens and the number of unique tokens in the respective lines processed by the loop, starting from the third line and processing every second line thereafter.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers, and prints the difference between the total number of integers and the number of unique integers in each test case.

