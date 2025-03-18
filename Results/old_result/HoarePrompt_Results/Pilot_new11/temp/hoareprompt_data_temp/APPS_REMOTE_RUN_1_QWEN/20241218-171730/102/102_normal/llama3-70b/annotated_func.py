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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is a positive integer, `b` is an integer, `x` and `y` are integers such that if the loop executed, the final values of `x` and `y` satisfy the equation `x * a + y * b == n`. If the loop does not execute, `x` remains 0 and `y` remains 0.
    print('NO')
#Overall this is what the function does:The function reads three integers `n`, `a`, and `b` from the standard input, where `1 ≤ n, a, b ≤ 10 000 000`. It then attempts to find non-negative integers `x` and `y` such that `x * a + y * b = n`. If such integers exist, it prints 'YES' followed by the values of `x` and `y` and exits. If no such integers exist, it prints 'NO'. The function does not accept any parameters and does not return any value. The final state of the program after execution is that it either prints 'YES' followed by `x` and `y` or 'NO', depending on whether a solution was found. Edge cases include when `n`, `a`, or `b` are at their minimum or maximum possible values, and the function handles these by ensuring that `x` and `y` remain within the valid integer range. However, the code does not explicitly check for `a` being zero, which would cause a division by zero error if `a` is zero and `n % a != 0`. Additionally, the code does not handle cases where `b` is zero, which would make the problem unsolvable if `n % a` is not divisible by `b`.

