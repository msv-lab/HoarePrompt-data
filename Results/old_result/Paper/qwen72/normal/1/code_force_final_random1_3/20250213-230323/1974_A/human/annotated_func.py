#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, x and y are integers where 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `x` is an input integer, `y` is an input integer, `a` is greater than or equal to the number of iterations, `i` is `a - 1`, `z` is `(y + 1) // 2`, and `m` is `15 * (y + 1) // 2 - y * 4`. If `m` < `a`, then `z` is updated to `(y + 1) // 2 + (x - m + 15 - 1) // 15.
#Overall this is what the function does:The function reads an integer `a` indicating the number of test cases. For each test case, it reads two integers `x` and `y`, computes a value `z` based on these inputs, and prints `z`. The computation of `z` involves adjusting its value based on a condition involving `m`, which is derived from `y` and `x`. After processing all test cases, the function has printed a result for each one, and the state of the program includes the processed values of `a`, `x`, `y`, and `z` for each iteration.

