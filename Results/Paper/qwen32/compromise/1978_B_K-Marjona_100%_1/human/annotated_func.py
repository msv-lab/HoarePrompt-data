#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print(b * k - k * (k - 1) // 2 + (n - k) * a)
        
    #State: t is an integer such that 1 <= t <= 10^4.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it calculates and prints a value based on these inputs. If `b` is less than or equal to `a`, it prints `a` multiplied by `n`. Otherwise, it computes a more complex expression involving `b`, `a`, and `n` and prints the result.

