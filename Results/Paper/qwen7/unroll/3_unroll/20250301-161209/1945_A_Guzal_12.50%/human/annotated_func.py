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
        
    #State: Output State: The value of `t` remains unchanged, and for each iteration of the loop, the variable `k` accumulates based on the conditions provided. Specifically, `k` is incremented by `a + (b + c) // 3`, and if `(b + c) % 3 != 0`, an additional 1 is added to `k`. If any of the conditions `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` are met during an iteration, -1 is printed instead of the value of `k`.
    #
    #Since the exact values of `n`, `a`, `b`, and `c` are not specified, the final value of `k` will depend on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers \(a\), \(b\), and \(c\) representing the number of introverts, extroverts, and universals, respectively. For each test case, it calculates and prints a value \(k\) based on specific conditions. If certain constraints are not met, it prints \(-1\) instead. The function does not return any value but prints the calculated \(k\) or \(-1\) for each test case.

