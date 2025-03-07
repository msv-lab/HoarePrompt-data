#State of the program right berfore the function call: The input is a series of test cases, each containing four lines with pairs of integers representing the coordinates of the corners of a square. Each coordinate pair (x_i, y_i) satisfies -1000 ≤ x_i, y_i ≤ 1000. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: The value of `res` squared for each iteration based on the conditions given in the loop. The final output state will be a list of these squared values, one for each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of four pairs of integer coordinates representing the corners of a square. For each test case, it checks if the square has sides parallel to the coordinate axes and a positive area. If the conditions are met, it calculates the side length of the square, squares it, and prints the result. The final output is a series of squared side lengths, one for each test case.

