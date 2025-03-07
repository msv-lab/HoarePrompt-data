#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each of the t test cases, there are four pairs of integers (x_i, y_i) where -1000 ≤ x_i, y_i ≤ 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop has executed `a` times, and for each iteration, it has read four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. For each square, it calculates the side length `res` based on the coordinates and prints `res
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It calculates and prints the area of each square.

