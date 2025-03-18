#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. Each integer from 1 to n appears at most twice in the list a. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The values of t, n, and a remain unchanged. The loop prints the difference between the number of elements in the list of tokens and the number of unique elements in the list of tokens for each even-indexed line from the input (excluding the first line).
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads input from the standard input, processes each even-indexed line (excluding the first line) by splitting the line into tokens, and prints the difference between the number of tokens and the number of unique tokens for each processed line. The state of any external variables `t`, `n`, and `a` remains unchanged.

