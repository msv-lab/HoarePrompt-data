#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def func():
    n, a, b = map(int, input().split())
    x = min(n, a, b)
    while True:
        if a >= x and b >= x and a - x + (b - x) >= x:
            break
        
        x -= 1
        
    #State of the program after the loop has been executed: `n` is an integer, `a` is an integer, `b` is an integer, and `x` is the largest integer such that `a >= x`, `b >= x`, and `a - x + (b - x) >= x`.
    print(x)
#Overall this is what the function does:The function reads three integers \( n \), \( a \), and \( b \) from standard input, where \( 1 \leq a, b \leq 100 \) and \( 2 \leq n \leq a + b \). It then finds the largest integer \( x \) such that \( a \geq x \), \( b \geq x \), and \( a - x + (b - x) \geq x \). The function prints this integer \( x \) as the output. The function handles edge cases where \( a \) or \( b \) might be equal to 1, and ensures that \( n \) is always valid within the given constraints. If no such \( x \) exists, the function will decrement \( x \) until it finds a valid solution or reaches 1.

