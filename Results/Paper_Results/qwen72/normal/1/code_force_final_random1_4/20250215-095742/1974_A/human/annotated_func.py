#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `x` and `y` are integers provided by user input, `a` is greater than or equal to the number of iterations completed, `i` is `a-1`, `z` is the final value of `(y + 1) // 2` after the last iteration, and `m` is the final value of `15 * ((y + 1) // 2) - y * 4` after the last iteration. If `m` < `a` during any iteration, then `z` is updated to `(y + 1) // 2 + (x - 15 * ((y + 1) // 2) + y * 4 + 14) // 15` for that iteration, and retains this value for subsequent iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. It first reads an integer `a` from the user, which represents the number of test cases. For each test case, it reads two integers `x` and `y` from the user. It then calculates a value `z` based on `y` and potentially adjusts `z` based on a condition involving `x` and `y`. Finally, it prints the calculated value of `z` for each test case. After the function completes, `a` is the total number of test cases processed, and `z` is the final value printed for the last test case. The function does not return any values; it only prints results.

