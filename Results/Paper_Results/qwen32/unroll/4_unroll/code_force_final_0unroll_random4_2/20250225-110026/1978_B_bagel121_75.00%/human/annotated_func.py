#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers n, a, and b such that 1 <= n, a, b <= 10^9.
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
        
    #State: t iterations have been completed, and for each iteration, the result of the calculation based on the input values n, a, and b has been printed. The variable t remains unchanged, and no other variables from the initial state are affected.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on the values of `n`, `a`, and `b`. Specifically, it computes the maximum possible sum of `n` integers where each integer is either `a` or `b`, with the constraint that no more than `b - a + 1` of the integers can be `b`.

