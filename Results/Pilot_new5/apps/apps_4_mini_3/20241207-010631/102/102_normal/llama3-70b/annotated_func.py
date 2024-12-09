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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a positive integer, `b` is between 1 and 10,000,000. The loop will iterate `n // a + 1` times, attempting to find non-negative integers `x` and `y` such that `x * a + y * b` equals `n`. If such values are found, the program prints 'YES', `x` is a non-negative integer representing how many times `a` fits into `n`, and `y` is a non-negative integer representing how many times `b` fits into the remaining portion of `n`. If no such values are found after all iterations, the program terminates without printing anything.
    print('NO')
#Overall this is what the function does:The function reads three integers `n`, `a`, and `b` from input. It checks if it is possible to express `n` as a non-negative linear combination of `a` and `b` by finding non-negative integers `x` and `y` such that `x * a + y * b = n`. If such integers are found, it prints 'YES' followed by the values of `x` and `y`. If no combination satisfies the equation after iterating through possible values of `x`, it prints 'NO'. If valid combinations are not possible (like when `a` and `b` are larger than `n`), the function may end up printing 'NO' without producing any meaningful output.

