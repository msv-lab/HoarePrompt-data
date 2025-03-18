#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most twice in the sequence a. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: The loop has processed all the lines in the input, and `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `a` is a list of `n` integers where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most twice in the sequence `a`. The sum of `n` over all test cases does not exceed 2 · 10^5.
#Overall this is what the function does:The function processes an input where each line represents a test case. For each test case, it reads a line, splits it into tokens, and prints the difference between the number of tokens and the number of unique tokens. The function does not modify the input parameters `t`, `n`, or `a`. After the function concludes, the input file has been fully read, and the output for each test case has been printed to the console.

