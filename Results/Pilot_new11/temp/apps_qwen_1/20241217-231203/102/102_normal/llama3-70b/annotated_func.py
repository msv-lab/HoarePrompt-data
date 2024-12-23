#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10 000 000, and n, a, and b are provided as inputs to the function.
def func():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        y = (n - x * a) // b
        
        if x * a + y * b == n:
            print('YES')
            print(x, y)
            exit()
        
    #State of the program after the  for loop has been executed: `a` is an integer, `b` is an integer, `n` is a non-negative integer, `x` is `n // a`, `y` is `(n - (n // a) * a) // b`. If `x * a + y * b == n` is satisfied, then 'YES' is printed to the console and the values of `x` and `y` are printed. Otherwise, no such pair of `x` and `y` is found.
    print('NO')
#Overall this is what the function does:The function `func()` accepts three integer inputs `n`, `a`, and `b` (all between 1 and 10,000,000). It attempts to find non-negative integers `x` and `y` such that `x * a + y * b = n`. If such a pair is found, the function prints "YES" followed by the values of `x` and `y` and then exits. If no such pair exists, the function prints "NO". The function does not return any value; it only outputs to the console. Potential edge cases include when `n` is less than `a` or `b`, or when `n` cannot be expressed as a linear combination of `a` and `b`.

