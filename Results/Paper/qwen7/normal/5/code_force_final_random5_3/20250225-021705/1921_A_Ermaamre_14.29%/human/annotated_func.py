#State of the program right berfore the function call: The function takes no input parameters. Each testcase is described over four lines, where each line contains two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. There are t such testcases, where 1 ≤ t ≤ 100, and it is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: a is an input integer, i is equal to a-1 (since the loop runs from 0 to a-1), x1, y1, x2, y2, x3, y3, x4, and y4 are input integers from the last iteration of the loop, and res is the absolute difference between y3 and y1 if x1 == x3 and x2 == x4 hold true, otherwise res is the absolute difference between y2 and y1 if x1 == x2 and x3 == x4 or x1 == x4 and x3 == x2 holds true, and res remains unchanged in other cases.
#Overall this is what the function does:The function processes a series of test cases, each defining a square with sides parallel to the coordinate axes. For each test case, it calculates the side length of the square by determining the vertical distance between two opposite corners. It then prints the square of this side length.

