#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: The loop has finished executing all iterations, and the values of t, n, a, and b are unchanged. However, the loop has printed the result of the conditional statements for each of the t test cases.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `a`, and `b` from the input. Depending on the values of `a` and `b`, it calculates and prints a result for each test case. The function does not return any value, but it prints the calculated result for each of the `t` test cases. After the function concludes, the values of `t`, `n`, `a`, and `b` are unchanged, and the program state is as it was before the function call, except for the printed outputs.

