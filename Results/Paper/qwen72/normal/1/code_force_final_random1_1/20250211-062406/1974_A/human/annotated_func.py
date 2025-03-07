#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `x` and `y` are integers provided by the user (0 <= x, y <= 99), `a` is the number of iterations the loop has run, `i` is `a - 1`, `z` is the final value computed by the loop for each iteration, which is `(y + 1) // 2` plus any adjustments made if `m < a`. The value of `m` is either `15 * z - y * 4` or remains unchanged if no adjustment was needed.
#Overall this is what the function does:The function `func` processes a series of test cases, where the number of test cases `a` is an integer such that 1 <= a <= 10^4. For each test case, it reads two integers `x` and `y` (0 <= x, y <= 99) from the user. It then computes a value `z` based on `y` and potentially adjusts it based on a condition involving `x` and `y`. The final value of `z` is printed for each test case. After the function concludes, the program state includes the number of test cases processed (`a`), the final values of `x` and `y` from the last test case, and the printed results for each test case.

