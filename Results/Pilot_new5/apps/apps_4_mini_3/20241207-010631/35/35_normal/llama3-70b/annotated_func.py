#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ a + b), a is an integer (1 ≤ a ≤ 100), and b is an integer (1 ≤ b ≤ 100).
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is the maximum value that satisfies `a >= x`, `b >= x`, and `a - x + (b - x) >= x`, and it is equal to its last valid state before the loop exited; `x` has been decremented to a value which is less than or equal to the original minimum of `n`, `a`, and `b`.
    print(x)
#Overall this is what the function does:The function accepts three integer parameters `n`, `a`, and `b` (where `2 ≤ n ≤ a + b`, `1 ≤ a ≤ 100`, and `1 ≤ b ≤ 100`) and determines the maximum integer `x` such that `x` is less than or equal to the minimum of `n`, `a`, and `b`, and also meets the condition `a >= x`, `b >= x`, and `a - x + (b - x) >= x`. The function prints this maximum valid value of `x`. If no valid value is found, it continues decrementing `x` until it reaches an invalid state. There is no explicit handling for cases where `x` could become negative, which could lead to an infinite loop if not properly bounded.

