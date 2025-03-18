#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is an integer representing the number of iterations, `x` and `y` are the integers from the last iteration, `z` is the value computed in the last iteration as `(y + 1) // 2 + (x - m + 14) // 15` if `m < a`, otherwise `(y + 1) // 2`, and `m` is the value computed in the last iteration as `15 * z - y * 4`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` (both between 0 and 99 inclusive), performs a series of calculations, and prints an integer `z` derived from these inputs.

