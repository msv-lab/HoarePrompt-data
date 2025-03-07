#State of the program right berfore the function call: The function `func` is expected to take input through a predefined method or variable, as the function definition does not specify any parameters. The input consists of multiple test cases, each containing four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square. The number of test cases, t, is an integer such that 1 ≤ t ≤ 100. Each coordinate x_i and y_i is an integer such that -1000 ≤ x_i, y_i ≤ 1000. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop will print the smaller of the two squared distances between the diagonally opposite corners of the square for each test case. After all iterations, the variables `steps`, `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `n`, and `x` will have their final values based on the last test case processed, but these values are not retained or meaningful outside the loop. The number of test cases `t` remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing the coordinates of the corners of a square. For each test case, it calculates the squared distances between two pairs of diagonally opposite corners of the square and prints the smaller of these two squared distances. The function does not return any values; instead, it directly prints the result for each test case. After processing all test cases, the function terminates, and the variables used within the loop are not retained or meaningful outside the loop. The number of test cases `t` remains unchanged.

