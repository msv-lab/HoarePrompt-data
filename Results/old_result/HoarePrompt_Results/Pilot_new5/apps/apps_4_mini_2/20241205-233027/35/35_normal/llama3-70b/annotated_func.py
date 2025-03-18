#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer such that 1 ≤ a ≤ 100, and b is an integer such that 1 ≤ b ≤ 100.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ `a` + `b`, `a` is an integer such that 1 ≤ `a` ≤ 100, `b` is an integer such that 1 ≤ `b` ≤ 100; `x` is the largest integer such that `x` was decremented to satisfy at least one of the conditions: `a >= x`, `b >= x`, or `a + b >= 2x`.
    print(x)
#Overall this is what the function does:The function accepts three integers `n`, `a`, and `b`, where `n` must be between 2 and the sum of `a` and `b`, while `a` and `b` are between 1 and 100. It calculates the largest integer `x` such that `x` is less than or equal to `n`, `a`, and `b`, and ensures that the remaining amounts from `a` and `b` after taking `x` are also at least `x`. The result `x` is printed as the output. There is no return value from the function.

