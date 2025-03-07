#State of the program right berfore the function call: The function should take a list of tuples as input, where each tuple represents the coordinates (x_i, y_i) of a corner of the square. The list contains exactly four tuples, and each x_i and y_i is an integer such that -1000 <= x_i, y_i <= 1000. The coordinates form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop will print the square of the side length of the square for each iteration, based on the coordinates provided in the input. The state of the variables `x1, y1, x2, y2, x3, y3, x4, y4, res` will be updated for each iteration, but their final values will depend on the last set of coordinates provided in the input. The variable `a` will remain unchanged.
#Overall this is what the function does:The function reads an integer `a` from the input, which determines the number of iterations. For each iteration, it reads four pairs of integer coordinates from the input, representing the corners of a square with sides parallel to the coordinate axes. The function calculates the side length of the square based on these coordinates and prints the square of the side length (i.e., the area of the square) for each iteration. The function does not return any value.

