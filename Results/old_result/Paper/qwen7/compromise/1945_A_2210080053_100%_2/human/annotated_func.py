#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively. After the loop executes all the iterations, for each test case, b has been updated to b + c, and the output prints (a - -b // 3, -1)[c < b % 3]. The values of a and c return to their initial states after each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing three non-negative integers \(a\), \(b\), and \(c\) representing the number of introverts, extroverts, and universals, respectively. For each test case, it updates \(b\) by adding \(c\) to it and then prints either \(\left(a - \left\lfloor\frac{b}{3}\right\rfloor\right)\) or \(-1\) based on whether \(c\) is less than \(b \mod 3\). After processing all test cases, the function does not return any value.

