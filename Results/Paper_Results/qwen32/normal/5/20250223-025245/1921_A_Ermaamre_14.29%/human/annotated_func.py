#State of the program right berfore the function call: The input consists of several test cases. The first line contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case consists of four lines, with each line containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop has executed `a` times, where `a` is the number of test cases. For each test case, the coordinates of the corners of a square are read, and the side length of the square is calculated as the absolute difference in the y-coordinates if two pairs of x-coordinates are equal, or in the x-coordinates if two pairs of y-coordinates are equal. The area of the square, which is the side length squared, is then printed. The variables `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`, and `res` are updated with the values from each test case during each iteration.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of the coordinates of the corners of a square. For each test case, it calculates and prints the area of the square.

