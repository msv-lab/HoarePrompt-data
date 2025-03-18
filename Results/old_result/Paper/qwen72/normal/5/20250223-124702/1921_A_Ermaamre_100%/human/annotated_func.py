#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates are such that -1000 <= x_i, y_i <= 1000, and there is a square with sides parallel to the coordinate axes and a positive area with corners at these points. The number of test cases, t, is an integer where 1 <= t <= 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The function will print the area of each square for each test case, calculated as the square of the difference between the maximum and minimum x-coordinates of the square's corners. The variable `t` will remain unchanged, and the variable `a` will contain the coordinates of the last processed square. The list `x` will contain the x-coordinates of the last processed square, and `dx` will contain the difference between the maximum and minimum x-coordinates of the last processed square.
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it reads four tuples of integers (x_i, y_i) representing the coordinates of the corners of a square. It then calculates and prints the area of the square for each test case, which is the square of the difference between the maximum and minimum x-coordinates of the square's corners. The function does not return any value. After the function concludes, the variable `t` remains unchanged, `a` contains the coordinates of the last processed square, `x` contains the x-coordinates of the last processed square, and `dx` contains the difference between the maximum and minimum x-coordinates of the last processed square.

