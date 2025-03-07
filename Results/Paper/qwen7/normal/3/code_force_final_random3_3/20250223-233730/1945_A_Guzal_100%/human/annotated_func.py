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
        
    #State: Postcondition: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` must be greater than 0, `i` is equal to `n-1`, `a`, `b`, and `c` are integers inputted from the user for each iteration, `k` accumulates the value of either `a + (b + c) // 3` or `a + (b + c) // 3 + 1` based on the conditions provided in the loop body, and the final output is the total sum of all `k` values calculated during the loop iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates a specific value based on certain conditions and prints the cumulative sum of these values. If a condition is not met, it prints -1 for that test case.

