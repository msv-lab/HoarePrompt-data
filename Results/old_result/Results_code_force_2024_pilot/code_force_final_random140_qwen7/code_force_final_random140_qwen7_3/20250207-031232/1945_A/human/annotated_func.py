#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\); `line` is the last line from the input; `p` is the first integer from the last line; `q` is the sum of the second and third integers from the last line plus the third integer from the last line; `r` is the third integer from the last line.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates and prints a value indicating the optimal seating arrangement based on the given numbers. The function does not return any value but prints the result for each test case.

