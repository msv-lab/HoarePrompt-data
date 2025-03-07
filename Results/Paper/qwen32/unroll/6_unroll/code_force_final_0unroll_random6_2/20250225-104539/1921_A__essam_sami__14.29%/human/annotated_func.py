#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there are four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The variable `t` remains unchanged, and for each of the `t` test cases, the program has printed the smaller of the two squared distances: either between points (a, b) and (e, f) or between points (c, d) and (g, h).
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads the coordinates of the corners of a square with sides parallel to the coordinate axes. It then calculates the squared distances between two pairs of opposite corners of the square and prints the smaller of the two squared distances.

