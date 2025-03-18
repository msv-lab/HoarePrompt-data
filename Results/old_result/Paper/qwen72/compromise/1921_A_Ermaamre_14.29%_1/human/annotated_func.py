#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, it should take four pairs of integers (x_i, y_i) (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. The coordinates are given in random order, but it is guaranteed that they form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: For each test case, the loop prints the square of the side length of the square formed by the given coordinates. The variables `x1, y1, x2, y2, x3, y3, x4, y4` and `res` are updated in each iteration, but their final values after the loop depends on the last test case input. The variable `a` remains unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it takes four pairs of integers (x_i, y_i) (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. The function then calculates and prints the area of the square for each test case. The final state of the program after the function concludes is that the areas of all the squares have been printed, and the variables `x1, y1, x2, y2, x3, y3, x4, y4`, and `res` are in their final states corresponding to the last test case. The variable `a` (which is `t`) remains unchanged.

