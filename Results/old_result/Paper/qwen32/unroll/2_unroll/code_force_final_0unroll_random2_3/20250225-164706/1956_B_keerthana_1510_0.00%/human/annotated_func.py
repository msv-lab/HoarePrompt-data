#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. The integer n appears at most twice in the list a_1, a_2, ..., a_n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        elements = line.split()
        
        print(sum(elements.count(item) // 3 for item in {*elements}))
        
    #State: 0 0
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates the sum of the integer divisions of the count of each unique element in the list by 3, and prints this sum.

