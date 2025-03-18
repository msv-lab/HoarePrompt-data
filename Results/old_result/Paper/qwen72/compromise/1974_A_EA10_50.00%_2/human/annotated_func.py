#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^4, and for each test case, x and y are integers where 0 <= x, y <= 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The loop prints the value of `z` for each iteration, and the values of `t`, `x`, `y`, and `a` remain unchanged after the loop finishes executing.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `x` and `y` from the input, where `0 <= x, y <= 99`. It then calculates a value `z` based on the formula `(y + 1) // 2` and adjusts `z` if a condition involving `m` (calculated as `15 * z - y * 4`) is met. The function prints the value of `z` for each test case. The function does not return any value. After the function concludes, the values of `t`, `x`, `y`, and `a` remain unchanged.

