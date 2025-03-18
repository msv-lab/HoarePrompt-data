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
        
    #State: Output State: The value of `k` is the sum of `a + (b + c) // 3` for each iteration where `(b + c) % 3 == 0` or `(b + c) % 3 != 0`, plus 1 if `(b + c) % 3 != 0`. If `b % 3 != 0 and b % 3 + c < 3`, the loop prints -1 and does not contribute to the final value of `k`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates and prints the maximum number of balanced seating arrangements possible. If a test case cannot achieve a balanced arrangement under certain conditions, it prints -1 instead. The function does not return any value but outputs the results for each test case.

