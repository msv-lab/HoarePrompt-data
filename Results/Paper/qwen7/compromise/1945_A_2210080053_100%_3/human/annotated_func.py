#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, where for each iteration, b is updated to b + c, and the print statement outputs (a - -b // 3, -1)[c < b % 3]. After all iterations, the values of a, b, and c for each test case are determined based on the operations performed within the loop.
#Overall this is what the function does:The function processes a series of test cases, where each test case includes three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it updates the number of extroverts by adding the number of universals and then calculates and prints the number of valid seating arrangements based on the adjusted number of extroverts and introverts. After processing all test cases, it outputs the calculated values for each case.

