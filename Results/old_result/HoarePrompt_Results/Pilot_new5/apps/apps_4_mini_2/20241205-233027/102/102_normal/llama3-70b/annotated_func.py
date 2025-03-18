#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 10,000,000; `a` is greater than 0; `x` is an integer in the range from 0 to `n // a`; `y` is an integer determined by the expression `(n - x * a) // b` for each `x`. The loop will either exit when a valid pair `(x, y)` is found such that `x * a + y * b = n`, or it will complete all iterations without finding such a pair, resulting in no output and the initial values of `x` and `y` being unmodified.
    print('NO')
#Overall this is what the function does:The function accepts three integer inputs `n`, `a`, and `b` from the user and checks if there are non-negative integer solutions `(x, y)` such that `x * a + y * b = n`. If such a pair is found, it prints 'YES' followed by the values of `x` and `y`. If no such pair exists after iterating through possible values of `x`, it prints 'NO'. The function does not return any value but communicates results via standard output.

