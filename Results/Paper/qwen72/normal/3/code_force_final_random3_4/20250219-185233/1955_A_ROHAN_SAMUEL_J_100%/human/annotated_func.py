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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, and for each of the `t` test cases, `n`, `a`, and `b` are integers such that 1 <= n <= 100 and 1 <= a, b <= 30. The loop variable `_` is `t - 1`. For each test case, if `n` is odd, then if 2 * a < b, the value `a * n` was printed; otherwise, the value `n // 2 * b + a` was printed. If `n` is even, then if 2 * a < b, the value `a * n` was printed; otherwise, the value `n // 2 * b` was printed.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by three integers `n`, `a`, and `b` where `1 <= n <= 100` and `1 <= a, b <= 30`. For each test case, the function computes and prints a value based on the following conditions: If `n` is odd, it prints `a * n` if `2 * a < b`, otherwise it prints `n // 2 * b + a`. If `n` is even, it prints `a * n` if `2 * a < b`, otherwise it prints `n // 2 * b`. The function processes up to `t` test cases, where `1 <= t <= 10^4`. After processing all test cases, the function does not return any value.

