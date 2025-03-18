#State of the program right berfore the function call: The input consists of several test cases. The first line contains one integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case is described by four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) which are the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive (strictly greater than 0) area.
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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the coordinates of the corners of two squares were read: (a, b), (c, d) for the first square, and (e, f), (g, h) for the second square. The distances squared from the center of the first square to the center of the second square were calculated as `n = (a - e) * (a - e) + (b - f) * (b - f)` and `x = (c - g) * (c - g) + (d - h) * (d - h)`. For each test case, the smaller of the two distances squared (`n` or `x`) was printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of the coordinates of the corners of two squares with sides parallel to the coordinate axes. For each test case, it calculates the squared distance from the center of one square to the center of the other square and prints the smaller of the two squared distances.

