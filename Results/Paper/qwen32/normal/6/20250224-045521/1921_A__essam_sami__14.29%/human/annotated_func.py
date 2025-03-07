#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each of the t test cases, there are four pairs of integers (x_i, y_i) where -1000 <= x_i, y_i <= 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop has executed `t` times, and for each iteration, it has printed the smaller value between `n` and `x`, where `n` is `(a - e) * (a - e) + (b - f) * (b - f)` and `x` is `(c - g) * (c - g) + (d - h) * (d - h)`. The variables `a, b, c, d, e, f, g, h` hold the values from the last iteration, and `steps` is equal to `t`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads the coordinates of the corners of a square and prints the area of the smaller square between two calculated values `n` and `x`.

