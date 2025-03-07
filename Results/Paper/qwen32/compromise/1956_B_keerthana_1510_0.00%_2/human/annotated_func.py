#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears at most 2 times in the sequence a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: 0 for each line processed by the loop
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of cards and the integers on those cards. For each test case, it calculates and prints the number of integers that appear at least three times across the cards.

