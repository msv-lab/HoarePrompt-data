#State of the program right berfore the function call: The function takes no input parameters. Each testcase is represented by four lines, where each line contains two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of the square. It is guaranteed that these points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: The loop will have executed all iterations specified by the initial value of `t`. After all iterations, `steps` will be equal to `t-1`, and the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` will each hold the last values they were assigned during the loop's final iteration. The variable `n` will be set to \((a - c)^2 + (b - d)^2\) and `x` will be set to \((a - e)^2 + (b - f)^2\). If `x` is greater than `n` during the last iteration, `n` will retain its value from the last iteration. Otherwise, `x` will retain its value from the last iteration. No other variables are changed outside of the loop, so their values remain as they were after the third iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four lines of input. Each line contains two integers \(x_i, y_i\) representing the coordinates of the corners of a square. For each test case, it calculates the squared distance between two pairs of opposite corners and prints the larger of the two distances. After processing all test cases, it outputs the results for each case.

