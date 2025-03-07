#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, n, a, and b are integers where 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: The loop has finished executing `t` iterations. For each iteration, the values of `n`, `a`, and `b` were read from input, and the corresponding result was printed. The variables `t`, `n`, `a`, and `b` are not retained after each iteration, and their final values are undefined.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each of the `t` test cases, it reads three integers `n`, `a`, and `b` from the input. If `a` is greater than or equal to `b`, it prints `n * a`. Otherwise, it calculates a value `ans` based on the minimum of `b - a + 1` and `n`, and prints the sum of `ans` and `(n - k) * a`, where `k` is the calculated minimum value. After processing all test cases, the function does not retain any of the input variables, and their final values are undefined. The function does not return any value.

