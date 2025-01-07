#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is the largest value that satisfies \(a \geq x\), \(b \geq x\), and \(a + b \geq 3x\), or it remains the minimum of `n`, `a`, and `b` if no such value exists; `a` and `b` retain their original values; `n` retains its original value.
    print(x)
#Overall this is what the function does:The function takes three integer inputs `n`, `a`, and `b` such that `1 ≤ a, b ≤ 100` and `2 ≤ n ≤ a + b`. It then finds the largest integer `x` that satisfies the conditions `a ≥ x`, `b ≥ x`, and `a + b ≥ 3x`. If no such `x` exists, it returns the minimum of `n`, `a`, and `b`. The function returns the value of `x`.

