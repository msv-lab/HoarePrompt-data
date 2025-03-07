#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if a >= b:
            print(n * a)
        else:
            k = min(b - a + 1, n)
            ans = int((b + (b - k + 1)) / 2 * k)
            p2 = (n - k) * a
            print(ans + p2)
        
    #State: Output State: All test cases specified by the initial integer `t` have been processed. For each test case, the output is determined based on the conditions provided within the loop. Specifically:
    #
    #- If `a >= b`, the output for each test case is `n * a`.
    #- If `a < b`, the output is calculated using the formula `ans + p2`, where:
    #  - `k` is the minimum value between `b - a + 1` and `n`.
    #  - `ans` is calculated as `int((b + (b - k + 1)) / 2 * k)`.
    #  - `p2` is `(n - k) * a`.
    #
    #The final output state will contain the results of all the test cases processed according to the rules described above.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it accepts three positive integers `n`, `a`, and `b`. Based on the relationship between `n`, `a`, and `b`, it calculates and prints the result for each test case. If `a >= b`, it prints `n * a`. Otherwise, it calculates `k` as the minimum of `b - a + 1` and `n`, then computes `ans` and `p2` using specific formulas and prints `ans + p2`. After processing all test cases, it outputs the results for each case according to the given conditions.

