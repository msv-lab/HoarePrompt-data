#State of the program right berfore the function call: The function should accept three parameters: n, a, and b, where n, a, and b are integers such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: The values of `n`, `a`, and `b` are not stored or modified outside the loop, so they do not have a final output state. The loop prints a result for each iteration based on the input values of `n`, `a`, and `b` provided during each iteration. The variable `t` remains unchanged after the loop execution.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads three integers `n`, `a`, and `b` from the input. Depending on the values of `a` and `b`, it calculates and prints a result for each test case. If `b` is less than or equal to `a`, it prints `n * a`. If `b - a` is greater than or equal to `n`, it prints `int((2 * b - n + 1) * n / 2)`. Otherwise, it prints `int((b - a) / 2 * (b - a + 1) + a * n)`. The function does not return any value. The variables `n`, `a`, and `b` are not stored or modified outside the loop, and the variable `t` remains unchanged after the loop execution.

