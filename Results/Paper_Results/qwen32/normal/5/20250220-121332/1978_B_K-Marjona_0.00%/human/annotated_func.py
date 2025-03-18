#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n, a, and b are positive integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: The loop has processed `t` test cases, and the last values of `n`, `a`, and `b` are those from the final iteration. The value of `t` remains as the initial input value but is no longer relevant to the loop control.
#Overall this is what the function does:The function processes a number of test cases specified by `t`. For each test case, it takes three integers `n`, `a`, and `b`, and prints a computed value based on these inputs. The computed value is determined by whether `b` is less than or equal to `a` or greater than `a`, using specific arithmetic operations to derive the result.

