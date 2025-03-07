#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, n, a, and b are positive integers such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: After all iterations of the loop have finished, `t` will be 0, and the values of `n`, `a`, and `b` will be updated to the last set of inputs provided by the user for each iteration. The loop processes each of the `t` test cases sequentially, updating `n`, `a`, and `b` with the new inputs for each case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three positive integers `n`, `a`, and `b`. It calculates and prints a result based on these inputs according to specific conditions. If `b` is less than or equal to `a`, it prints `n * a`. If `b - a` is greater than or equal to `n`, it prints the sum of an arithmetic series starting from `2 * b - n + 1` with `n` terms divided by 2. Otherwise, it prints the sum of the first part of an arithmetic series from `b - a` plus `a * n`. After processing all test cases, the variable `t` is set to 0, and the values of `n`, `a`, and `b` are updated to the last set of inputs provided.

