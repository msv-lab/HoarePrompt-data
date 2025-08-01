#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of a corner of the square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and there is exactly one square with sides parallel to the coordinate axes and a positive area for each test case. The number of test cases, t, satisfies 1 <= t <= 100.
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: `t` is an integer greater than 2 and less than or equal to 100, `steps` is `t-1`, `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` are the last set of input integers for the final iteration, `n` is equal to \((a - e)^2 + (b - f)^2\), and `x` is equal to \((c - g)^2 + (d - h)^2\). If `x` > `n`, then `x` is greater than `n`. Otherwise, `x` is less than or equal to `n`.
#Overall this is what the function does:The function reads a series of test cases from user input, where each test case consists of four pairs of integers representing the coordinates of the corners of a square. For each test case, it calculates two distances: `n` between the first and third points, and `x` between the second and fourth points. It then prints the smaller of these two distances for each test case. After processing all test cases, the function concludes with `t` being an integer between 1 and 100, `steps` being `t-1`, and the last set of input coordinates being stored in `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h`. The final state includes the printed results for each test case.

