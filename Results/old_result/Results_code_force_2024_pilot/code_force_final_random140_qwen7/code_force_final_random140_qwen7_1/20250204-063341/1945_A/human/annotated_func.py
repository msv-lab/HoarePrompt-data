#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: Output State: After all iterations of the loop have finished, `p` will be an integer that started as a positive integer (1 ≤ t ≤ 10^4) minus the total number of times `q // 3` was added across all iterations, and `q` will be the sum of all `q` values from each iteration. The value of `r` will be the sum of all `r` values from each iteration.
    #
    #This means that for each line processed, `p` is decreased by one-third of `q` rounded down, and `q` and `r` are updated based on the current line's values before moving to the next line.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it updates the value of `p` by subtracting one-third of `q` (where `q` is initially the sum of the second and third integers of the test case, and then incremented by the third integer) from `p`. The final state of `p` is the initial value minus the cumulative subtraction across all test cases. The function prints the result of this calculation for each test case.

