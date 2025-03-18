#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2 · 10^5, representing the number of cards each player receives. a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ n, representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the sequence a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: For each test case, the loop prints the number of unique integers in the sequence a_1, a_2, ..., a_n that appear at least three times. The variables t, n, and the sequence a_1, a_2, ..., a_n remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases from the standard input. Each test case includes a sequence of integers representing cards in your hand. The function prints the number of unique integers in each sequence that appear at least three times. The function does not modify the input variables or return any value.

