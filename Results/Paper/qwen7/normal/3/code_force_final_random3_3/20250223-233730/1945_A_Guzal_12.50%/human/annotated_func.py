#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is the total number of iterations the loop executed, `i` is equal to `n - 1`, `a`, `b`, and `c` are integers obtained from the input split by spaces for the last iteration, `k` is the final value calculated based on the conditions in the loop body for the last iteration, and all previous `k` values are printed as per the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates a value `k` based on specific conditions involving these integers. If the conditions are met, it prints the value of `k`; otherwise, it prints `-1`. The function does not return any value explicitly but prints the results for each test case.

