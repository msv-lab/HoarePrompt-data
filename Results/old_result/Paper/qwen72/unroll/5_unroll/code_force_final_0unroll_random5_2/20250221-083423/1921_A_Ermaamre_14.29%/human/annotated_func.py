#State of the program right berfore the function call: The function should take a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and the number of test cases t satisfies 1 <= t <= 100. The coordinates are guaranteed to form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: The loop will print the area of each square provided in the test cases, calculated as the square of the side length. The variable `a` will remain unchanged, and the loop will have iterated `a` times. The variables `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`, and `res` will have their final values based on the last iteration of the loop.
#Overall this is what the function does:The function reads an integer `a` from the user, which represents the number of test cases. For each test case, it reads four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square. The function then calculates and prints the area of each square, which is the square of the side length. The function does not return any value. After the function concludes, the variable `a` remains unchanged, and the loop has iterated `a` times, with the final values of `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`, and `res` based on the last iteration.

