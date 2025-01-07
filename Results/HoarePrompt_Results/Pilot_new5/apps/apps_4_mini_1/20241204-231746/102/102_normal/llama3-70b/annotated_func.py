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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is an integer such that 1 ≤ a ≤ 10,000,000, `x` is equal to `n // a`, `y` is equal to `(n - x * a) // b` if `x * a + y * b` equals `n`, and the program prints 'YES' along with the values of `x` and `y`. If no such `x` and `y` satisfy the condition, the loop will have executed `n // a + 1` times and no output will be printed.
    print('NO')
#Overall this is what the function does:The function accepts no parameters and reads three integers, `n`, `a`, and `b`, from input. It checks if `n` can be expressed as a linear combination of `a` and `b` using non-negative integers `x` and `y`. If such a combination exists, it prints 'YES' followed by the values of `x` and `y`; otherwise, it prints 'NO'. The function does not return any values.

