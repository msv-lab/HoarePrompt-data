#State of the program right berfore the function call: The function `func` is expected to take input in the form of multiple test cases, where each test case consists of four pairs of integers representing the coordinates of the corners of a square. The coordinates are within the range -1000 to 1000, inclusive, and the square has a positive area with sides parallel to the coordinate axes. The number of test cases, `t`, is an integer such that 1 <= t <= 100.
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
        
    #State: The loop will print the square of the side length of the square for each test case. The variables `x1, y1, x2, y2, x3, y3, x4, y4` will have their final values as the coordinates of the last test case, and `res` will be the side length of the last square. The variable `a` will remain unchanged.
#Overall this is what the function does:The function `func` accepts multiple test cases, each containing four pairs of integers representing the coordinates of the corners of a square. For each valid test case, it prints the area of the square. The function assumes the input coordinates form a valid square with sides parallel to the coordinate axes and within the specified range. If the input does not form a valid square, the function may produce incorrect results, but it does not explicitly handle or report invalid input. After processing all test cases, the function does not return any value, and the final state of the program includes the coordinates of the last test case and the side length of the last square.

