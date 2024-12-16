#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10 000 000.
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
        
    #State of the program after the  for loop has been executed: ``x` is either the value that satisfies `x * a + y * b == n` or `n // a`, `y` is either the value that satisfies `x * a + y * b == n` or `0`, `n` is an integer obtained from `int(input())`, `a` is an integer input from the user, and `b` is an integer obtained from `int(input())
    print('NO')
#Overall this is what the function does:The function reads three integers `n`, `a`, and `b` from the user and checks if there exist non-negative integers `x` and `y` such that `x * a + y * b = n`. If such a pair is found, it prints "YES" followed by the values of `x` and `y` and exits. If no such pair exists, it prints "NO".

