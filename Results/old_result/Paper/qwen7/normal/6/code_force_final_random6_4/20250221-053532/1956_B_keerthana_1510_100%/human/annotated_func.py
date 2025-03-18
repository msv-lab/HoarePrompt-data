#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 to n appears at most twice in the list a.
def func():
    for line in [*open(0)][2::2]:
        print(len((tokens := line.split())) - len({*tokens}))
        
    #State: Output State: The loop has executed all its iterations, meaning it has processed every line of input that fits the specified pattern (every second line starting from the third line). `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is a positive integer such that \(1 \leq n \leq 2 \cdot 10^5\), `a` is a list containing `n` integers such that \(1 \leq a_i \leq n\) and each integer from 1 to `n` appears at most twice in the list `a`, and there are no more lines left to process according to the loop's condition.
    #
    #In simpler terms, the loop has gone through all valid input lines, and now the program is ready to terminate or proceed with any post-loop operations.
#Overall this is what the function does:The function processes standard input, specifically every second line starting from the third line, which should contain space-separated integers. For each line, it calculates and prints the number of unique tokens (integers) present, excluding duplicates. After processing all valid input lines, the function concludes with no return value.

