#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is the number of iterations which is greater than 0, `i` equals `a`, `x` and `y` are the integers from the last iteration, `z` is the value computed in the last iteration, and `m` is the value of `m` computed in the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y`. It then computes and prints a value `z` based on the values of `x` and `y`.

