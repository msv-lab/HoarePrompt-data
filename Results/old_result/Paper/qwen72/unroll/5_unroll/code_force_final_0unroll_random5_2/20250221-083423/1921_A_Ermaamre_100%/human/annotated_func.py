#State of the program right berfore the function call: The function should take a list of test cases as input, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates x_i and y_i satisfy -1000 <= x_i, y_i <= 1000, and the points form a square with sides parallel to the coordinate axes and a positive area. The number of test cases, t, satisfies 1 <= t <= 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The loop will print the area of each square for each test case. The variable `t` will remain unchanged, and the variable `a` will contain the coordinates of the last square processed. The variable `x` will contain the x-coordinates of the last square processed, and `dx` will contain the side length of the last square processed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads four tuples of coordinates (x_i, y_i) representing the corners of a square. The function then calculates and prints the area of the square for each test case. After the function concludes, the variable `t` remains unchanged, and the variables `a`, `x`, and `dx` contain the coordinates, x-coordinates, and side length of the last square processed, respectively. The function does not return any value.

