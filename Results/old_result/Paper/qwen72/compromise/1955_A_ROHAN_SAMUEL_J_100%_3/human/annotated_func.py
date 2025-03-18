#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
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
        
    #State: The values of t, n, a, and b remain unchanged, but the loop has printed the calculated values for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer such that 1 <= t <= 10^4. For each test case, it reads integers `n`, `a`, and `b` (1 <= n <= 100 and 1 <= a, b <= 30) from the input. It then calculates and prints a result based on the following conditions: If `n` is odd and `2 * a` is less than `b`, it prints `a * n`. If `n` is odd and `2 * a` is not less than `b`, it prints `n // 2 * b + a`. If `n` is even and `2 * a` is less than `b`, it prints `a * n`. If `n` is even and `2 * a` is not less than `b`, it prints `n // 2 * b`. The values of `t`, `n`, `a`, and `b` are not modified by the function.

