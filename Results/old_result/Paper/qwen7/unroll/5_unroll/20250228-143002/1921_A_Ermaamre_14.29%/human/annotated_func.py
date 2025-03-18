#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are \(t\) such sets of coordinates, where \(1 \le t \le 100\).
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
        
    #State: Output State: The value of `res` squared after all iterations of the loop have finished, based on the conditions provided in the loop body. Each iteration of the loop calculates the absolute difference between two y-coordinates and squares the result, then prints it.
#Overall this is what the function does:The function processes \(t\) sets of coordinates, each containing four points representing the corners of a square. It checks if the given coordinates form a valid square by comparing the x and y coordinates. For each valid square, it calculates the vertical distance between two opposite corners, squares this distance, and prints the result. The function does not return any value but prints the squared distance for each valid square found.

