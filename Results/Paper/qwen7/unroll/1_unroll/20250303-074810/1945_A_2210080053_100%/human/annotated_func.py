#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a', b', and c' where a' is the result of (a - -b // 3) if c' >= b % 3, otherwise it's just a - -b // 3, b' is the result of b + c, and c' is the original value of c from the input.
#Overall this is what the function does:The function processes a series of test cases, each containing the counts of introverts (a), extroverts (b), and universals (c). For each test case, it calculates the adjusted count of introverts based on the number of extroverts and universals, and prints the result. Specifically, it computes the adjusted introverts count as \(a - \left\lfloor\frac{b + c}{3}\right\rfloor\) if the remainder when \(b + c\) is divided by 3 is less than or equal to the number of universals, otherwise it uses \(a - \left\lfloor\frac{b}{3}\right\rfloor\). The function outputs this adjusted count for each test case.

