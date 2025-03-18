#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the next t lines contains three integers n, a, and b, where 1 <= n <= 100, 1 <= a, b <= 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each iteration, the values of `n`, `a`, and `b` were read from the input. Depending on whether `n` is odd or even and the relationship between `2 * a` and `b`, the output was either `a * n` or `n // 2 * b + a` (for odd `n` when `2 * a >= b`) or `n // 2 * b` (for even `n` when `2 * a >= b`). The final output state is the result of all these individual outputs for each iteration.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a result based on whether `n` is odd or even and the relationship between `2 * a` and `b`.

