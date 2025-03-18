#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and there is exactly one square with sides parallel to the coordinate axes and a positive area for each test case. The number of test cases, t, satisfies 1 <= t <= 100.
def func():
    a = int(input())
    for i in range(a):
        x1, y1 = map(int, input().split())
        
        x2, y2 = map(int, input().split())
        
        x3, y3 = map(int, input().split())
        
        x4, y4 = map(int, input().split())
        
        if x1 == x3 and x2 == x4:
            if y1 < y3:
                res = abs(y3 - y1)
            else:
                res = abs(y1 - y3)
        elif x1 == x2 and x3 == x4:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        elif x1 == x4 and x3 == x2:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        
        print(res ** 2)
        
    #State: `a` is greater than or equal to the number of iterations, `i` is `a-1`, and for each iteration, `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, and `y4` are input integers. If `x1 == x3` and `x2 == x4`, then if `y1 < y3`, `res` is the absolute difference between `y3` and `y1`. If `y1` is greater than or equal to `y3`, `res` is the absolute difference between `y1` and `y3`. If `x1 == x2` and `x3 == x4`, or if `x1 == x4` and `x3 == x2`, then `res` is the absolute difference between `y1` and `y2`. For each iteration, the square of `res` is printed.
#Overall this is what the function does:The function `func` reads a series of test cases from the input. Each test case consists of four pairs of coordinates (x_i, y_i) representing the corners of a square. The function calculates the side length of the square by finding the absolute difference between the y-coordinates of the appropriate pairs of points. It then prints the area of the square (side length squared) for each test case. The function does not return any value; it only prints the results. After the function concludes, the input coordinates have been processed, and the areas of the squares have been printed for each test case.

