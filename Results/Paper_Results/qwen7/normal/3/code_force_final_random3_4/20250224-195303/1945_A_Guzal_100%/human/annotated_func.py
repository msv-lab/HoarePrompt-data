#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: Output State: After the loop executes all iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is the total number of iterations the loop has executed, `i` will be equal to `n - 1` (since the loop increments `i` from 0 to `n-1`), and `k` will be the sum of `a + (b + c) // 3 + 1` for each iteration where `b % 3 != 0 and b % 3 + c < 3` is false, otherwise it will be `a + (b + c) // 3`.
    #
    #In simpler terms, `k` accumulates the value of `a + (b + c) // 3 + 1` for each iteration unless the condition `b % 3 != 0 and b % 3 + c < 3` is met, in which case `k` does not increment. The final value of `k` is the sum of these values over all iterations.
#Overall this is what the function does:The function processes a series of test cases, each containing the counts of introverts (a), extroverts (b), and universals (c). For each test case, it calculates a value `k` based on specific conditions involving `a`, `b`, and `c`. If certain conditions are not met, `k` is incremented by `a + (b + c) // 3 + 1`; otherwise, it only includes `a + (b + c) // 3`. The function outputs `k` for each test case and returns the cumulative sum of all `k` values after processing all test cases.

