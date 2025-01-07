#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ a, b ≤ 100, 2 ≤ n ≤ a + b.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: 'x' is 0, 'a' is greater than or equal to 'x', 'b' is greater than or equal to 'x', 'n' is within the range [2, a+b] inclusive, and the condition \(a \geq x\) and \(b \geq x\) and \((a - x + (b - x)) \geq x\) holds.
    print(x)
#Overall this is what the function does:The function reads three integers `n`, `a`, and `b` from the user, and returns the largest integer `x` such that `x` is less than or equal to the minimum of `a` and `b`, and `a - x + (b - x) >= x`.

