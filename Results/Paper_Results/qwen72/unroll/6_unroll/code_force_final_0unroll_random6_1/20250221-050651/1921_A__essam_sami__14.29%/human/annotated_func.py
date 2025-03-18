#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and the square has a positive area with sides parallel to the coordinate axes. The number of test cases, t, satisfies 1 <= t <= 100.
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
        
    #State: The loop will print the minimum of the squared distances between the corresponding corners of the two squares for each test case. The variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` will retain their final values from the last iteration of the loop, and `n` and `x` will retain their final computed values from the last iteration. The number of test cases `t` will remain unchanged.
#Overall this is what the function does:The function reads a series of test cases from the user input, where each test case consists of the coordinates of the corners of two squares. For each test case, it calculates the squared distances between the corresponding corners of the two squares and prints the minimum of these squared distances. The function does not return any value; it only prints the results. After the function concludes, the number of test cases `t` remains unchanged, and the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `n`, and `x` retain their final values from the last iteration of the loop.

