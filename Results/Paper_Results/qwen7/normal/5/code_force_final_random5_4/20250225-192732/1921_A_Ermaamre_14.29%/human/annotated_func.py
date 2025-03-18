#State of the program right berfore the function call: There are four lines, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: The loop will execute `a` times, where `a` is the initial integer input. After all iterations, the variable `res` will hold the result of the last calculation performed within the loop. Specifically, `res` will be the absolute difference between two specific `y` values based on the conditions provided, corresponding to the last set of inputs processed in the loop. The variable `i` will be equal to `a-1` after all iterations, indicating the completion of the loop. All other variables (`x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`) will retain their values from the last iteration of the loop.
    #
    #In natural language: After the loop completes all its iterations, `res` will contain the final calculated value based on the conditions given for the last set of inputs processed. The variable `i` will be equal to `a-1`, signifying the end of the loop. The values of `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, and `y4` will reflect the last inputs provided to the loop.
#Overall this is what the function does:The function processes a series of square corner coordinates and calculates the height of the tallest vertical line segment among them. It accepts no parameters and returns nothing, instead printing the squared height of the tallest vertical line segment for each set of coordinates provided. After processing all sets of coordinates, it prints the squared height of the tallest vertical line segment found in the last set of inputs.

