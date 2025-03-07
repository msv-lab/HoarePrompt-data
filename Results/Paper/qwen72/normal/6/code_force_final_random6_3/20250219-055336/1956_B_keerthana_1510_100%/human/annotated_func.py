#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most twice. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ n, with each integer from 1 to n appearing at most twice, and the input to file descriptor `0` must contain at least 2t + 1 lines.
#Overall this is what the function does:The function `func` reads from the standard input (file descriptor `0`), processing every third line starting from the third line. For each processed line, it calculates the difference between the number of tokens (words) and the number of unique tokens in the line, and prints this difference. The function does not return any value. The state of the program after the function concludes is unchanged except for the side effect of printing the calculated differences for each line.

