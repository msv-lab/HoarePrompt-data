#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n // 2))
        else:
            print(int((b - a) * (b - a + 1) // 2 + a * n))
        
    #State: After the loop executes all the iterations, `t` is set to 0, indicating that all test cases have been processed. The variables `n`, `a`, and `b` are reset to the values of the last test case that was processed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three positive integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on the given conditions. After processing all test cases, the variable `t` is set to 0, indicating completion.

