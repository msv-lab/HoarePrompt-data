#State of the program right berfore the function call: There are four lines, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - c) * (a - c) + (b - d) * (b - d)
        
        x = (a - e) * (a - e) + (b - f) * (b - f)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: After the loop executes all iterations, `t` must be equal to the number of iterations executed, `steps` is `t-1`, `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` will hold the last set of input values provided by the user, `n` will be the minimum value between the last calculated `n` and `x`, and `x` will be the last calculated value of `(a - e) * (a - e) + (b - f) * (b - f)` compared to the previous `n`.
#Overall this is what the function does:The function reads multiple sets of four coordinates from the user, calculates the squared distance between the first and third coordinates, and then compares it with the squared distance between the first and fourth coordinates. It prints the smaller of these two distances after each comparison. After processing all inputs, it does not return anything but leaves the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` holding the last set of input values, and `n` and `x` holding the minimum squared distance found during the comparisons.

