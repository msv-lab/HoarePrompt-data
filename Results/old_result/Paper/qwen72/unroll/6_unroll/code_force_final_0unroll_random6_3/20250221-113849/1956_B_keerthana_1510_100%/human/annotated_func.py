#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The function should take parameters `t` (number of test cases), and for each test case, `n` (number of cards each player receives) and `a` (list of integers representing the cards in your hand). The parameters should satisfy: 1 ≤ t ≤ 10^4, 1 ≤ n ≤ 2 · 10^5, and 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most twice in `a`.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: For each test case, the loop prints the number of duplicate card values in the list `a` for that test case. The function `func` remains incomplete and does not match the problem description. The parameters `t`, `n`, and `a` are not modified by the loop.
#Overall this is what the function does:The function `func` reads input from the standard input, processes each test case by counting the number of duplicate card values in the list `a` for that test case, and prints the count. The function does not modify the parameters `t`, `n`, or `a`. It does not return any value.

