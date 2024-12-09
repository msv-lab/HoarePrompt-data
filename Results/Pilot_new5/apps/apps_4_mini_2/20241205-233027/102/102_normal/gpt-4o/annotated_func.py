#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `a` is an input integer such that 1 ≤ `a` ≤ 10,000,000; `b` is an input integer; `n` is greater than or equal to 0; `x` is `n // a`; if there exists a non-negative integer `y` such that `n = x * a + y * b`, then `y` is the corresponding value; otherwise, no valid `(x, y)` pairs are found.
    print('NO')
#Overall this is what the function does:The function accepts three integers `n`, `a`, and `b`, checks for non-negative integer solutions `(x, y)` such that `n = x * a + y * b`, prints 'YES' and the corresponding values if a solution exists, or prints 'NO' if no solution is found. The function does not return any value.

