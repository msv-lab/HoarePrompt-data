#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    for s in [*open(0)][1:]:
        a, b, c = map(int, s.split())
        
        b += c
        
        print((a - -b // 3, -1)[c < b % 3])
        
    #State: After the loop executes all the iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `b` is the sum of its original value and all `c` values encountered during the loop, `a` is the total sum of all `a` values encountered during the loop, and `c` is the total sum of all `c` values encountered during the loop. The variable `s` contains the last line of input read from the input stream before the loop completes.
#Overall this is what the function does:The function processes multiple test cases, each containing three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it updates the count of extroverts by adding the count of universals and then calculates and prints a result based on the adjusted counts of introverts and extroverts. The function does not return any value but prints the result for each test case.

