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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, and for each test case, `n`, `a`, and `b` are integers such that 1 <= n <= 100 and 1 <= a, b <= 30. The loop variable `_` is equal to `t - 1`. If `n` is odd, the condition `2 * a < b` holds if `2 * a` is less than `b`, and the condition `2 * a >= b` holds if `2 * a` is greater than or equal to `b`. If `n` is even, the condition `2 * a < b` holds if `2 * a` is less than `b`, and the condition `2 * a >= b` holds if `2 * a` is greater than or equal to `b`.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` from input, which represents the number of test cases, where 1 <= t <= 10^4. For each test case, it reads three integers `n`, `a`, and `b` from input, where 1 <= n <= 100 and 1 <= a, b <= 30. The function calculates and prints a result for each test case based on the following rules: If `n` is odd, it prints `a * n` if `2 * a < b`, otherwise it prints `n // 2 * b + a`. If `n` is even, it prints `a * n` if `2 * a < b`, otherwise it prints `n // 2 * b`. After processing all test cases, the function concludes without returning any value.

