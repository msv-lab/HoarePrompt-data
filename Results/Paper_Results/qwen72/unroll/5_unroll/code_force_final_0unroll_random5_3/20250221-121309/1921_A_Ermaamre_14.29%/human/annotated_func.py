#State of the program right berfore the function call: The function `func` is expected to take input through standard input (stdin) and output through standard output (stdout). The input includes an integer t (1 ≤ t ≤ 100) representing the number of test cases, followed by t test cases, each containing four lines with two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) per line, representing the coordinates of the corners of a square. It is guaranteed that the coordinates form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: The loop will print the area of each square for each test case, calculated as the square of the side length. The side length is determined by the absolute difference in the y-coordinates of the given points, assuming the points form a square with sides parallel to the coordinate axes. The variables `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`, and `i` will be updated within the loop, but their final values after the loop ends are not relevant to the output state. The variable `a` will remain unchanged.
#Overall this is what the function does:The function `func` reads from standard input (stdin) an integer `t` representing the number of test cases, followed by `t` test cases, each containing the coordinates of four corners of a square. It calculates and prints the area of each square to standard output (stdout). The area is computed as the square of the side length, which is determined by the absolute difference in the y-coordinates of the given points, assuming the points form a square with sides parallel to the coordinate axes. The function does not return any value; it only prints the results.

