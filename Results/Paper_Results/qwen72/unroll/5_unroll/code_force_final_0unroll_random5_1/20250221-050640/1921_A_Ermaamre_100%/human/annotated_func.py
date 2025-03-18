#State of the program right berfore the function call: The function should take a list of test cases as input, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates (x_i, y_i) satisfy -1000 <= x_i, y_i <= 1000, and the number of test cases t satisfies 1 <= t <= 100. The coordinates are guaranteed to form a square with sides parallel to the coordinate axes and with a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The loop will print the area of each square for each test case, calculated as the square of the side length (which is the difference between the maximum and minimum x-coordinates of the square's corners). The variable `t` will remain unchanged, and the list of test cases will also remain unchanged. The variables `a`, `x`, and `dx` will be overwritten in each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads four tuples of coordinates (x_i, y_i) from the input, where each tuple represents a corner of a square. The function calculates the side length of the square by finding the difference between the maximum and minimum x-coordinates of the corners, and then prints the area of the square, which is the square of the side length. The function does not return any value. After the function concludes, the variable `t` remains unchanged, and the input test cases are processed and the areas of the squares are printed. The internal variables `a`, `x`, and `dx` are overwritten in each iteration of the loop.

