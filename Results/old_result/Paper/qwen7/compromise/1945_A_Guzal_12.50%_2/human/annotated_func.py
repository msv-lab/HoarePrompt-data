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
        
    #State: Output State: The value of `t` remains unchanged, and for each iteration of the loop, the variable `k` accumulates based on the conditions provided. Specifically, `k` is incremented by `a + (b + c) // 3`, and if `(b + c) % 3 != 0`, an additional 1 is added to `k`. If any input does not meet the specified conditions, `-1` is printed instead of updating `k`. After all iterations, the final value of `k` is the sum of all valid updates across the iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers a, b, and c. For each test case, it calculates a value k based on specific conditions involving a, b, and c. If the conditions are met, k is updated accordingly; otherwise, -1 is printed. After processing all test cases, the final value of k is the sum of all valid updates across the iterations. The function prints the value of k for each test case and returns no explicit value.

