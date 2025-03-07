#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each of the t test cases, there are four pairs of integers (x_i, y_i) where -1000 ≤ x_i, y_i ≤ 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: For each of the `t` test cases, the output will be the smaller of the two squared distances calculated between the given pairs of points.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. Each test case consists of four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. For each test case, the function calculates the squared distances between two pairs of these points and prints the smaller of the two squared distances.

