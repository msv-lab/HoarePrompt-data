#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each of the t test cases, there are four lines, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The output state consists of `a` lines, each line containing the area of a square calculated from the input coordinates for each of the `a` test cases. The variables `t` and `a` remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It then calculates and prints the area of the square for each test case.

