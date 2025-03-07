#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4, and for each test case, n, a, and b are integers such that 1 \le n, a, b \le 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop has executed `t` times, and for each test case, `n`, `a`, and `b` are input integers such that 1 ≤ n, a, b ≤ 10^9. The variable `_` is `t - 1`, and for each iteration, `k` is the minimum of `n` and `b - a`. If `b` is less than or equal to `a`, the output for that test case is `a * n`. Otherwise, the output for that test case is `((b + (b - k + 1)) // 2) * k + (n - k) * a`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `a`, and `b`. It then calculates and prints a result based on these inputs. If `b` is less than or equal to `a`, the result is `a * n`. Otherwise, the result is `((b + (b - k + 1)) // 2) * k + (n - k) * a`, where `k` is the minimum of `n` and `b - a`. After processing all `t` test cases, the function completes, and the final state is that `t` lines of output have been printed, each corresponding to the result of a test case.

