#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After the loop executes all iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\), and there are exactly `t` lines of input processed. For each line, `a` is the first integer, `b` is the second integer plus the third integer, and `c` is the third integer. The loop processes each line sequentially, updating `b` by adding `c` and printing the result of `(a - -b // 3, -1)[c < b % 3]` for each line.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of three non-negative integers a, b, and c. It updates b by adding c and then prints the result of a specific calculation involving a and b. The function does not return any value but prints the result for each test case. If a test case is invalid (i.e., the values of a, b, or c do not meet the specified conditions), it does not produce an error message but simply moves on to the next test case.

