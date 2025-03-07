#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case consists of four lines, with each line containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The areas of all `a` squares, each printed on a new line.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads the coordinates of the corners of a square and prints the area of the square.

