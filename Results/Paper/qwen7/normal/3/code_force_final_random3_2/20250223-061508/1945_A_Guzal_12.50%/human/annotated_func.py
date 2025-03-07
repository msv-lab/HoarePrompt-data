#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c representing the number of introverts, extroverts, and universals, respectively, such that 0 ≤ a, b, c ≤ 10^9.
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
        
    #State: Output State: The value of `k` after the loop executes all iterations will be the sum of `a + (b + c) // 3` for each iteration where the condition `(b + c) % 3 != 0` and both `b % 3 != 0` and `c < 3` are satisfied, plus an additional 1 for each such iteration.
    #
    #In simpler terms, `k` accumulates the value of `a + (b + c) // 3` from each iteration, adding 1 to `k` whenever the specific conditions are met during those iterations. The final value of `k` is the total sum of these contributions across all iterations.
#Overall this is what the function does:The function processes multiple sets of three non-negative integers \(a\), \(b\), and \(c\) representing the counts of introverts, extroverts, and universals respectively. For each set, it calculates a value based on specific conditions involving \(b\) and \(c\). If certain conditions are met, it increments a cumulative count \(k\). Finally, it prints the accumulated value \(k\) for each set of inputs.

