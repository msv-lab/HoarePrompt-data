#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The integers x_i and y_i satisfy -1000 <= x_i, y_i <= 1000, and each test case is guaranteed to represent a square with sides parallel to the coordinate axes and a positive area. The number of test cases, t, satisfies 1 <= t <= 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The loop will print the area of each square (which is the side length squared) for each test case. The variable `t` will remain unchanged, and the list of test cases will also remain unchanged. The variables `a`, `x`, and `dx` will be overwritten in each iteration, but their final values after the loop will be those from the last test case.
#Overall this is what the function does:The function `func` reads a series of test cases from the user input. Each test case consists of four tuples representing the coordinates of the corners of a square. For each test case, the function calculates the side length of the square by finding the difference between the maximum and minimum x-coordinates. It then prints the area of the square, which is the side length squared. The function does not return any value; it only prints the areas of the squares for each test case. The variable `t` (number of test cases) remains unchanged, and the list of test cases is not stored or modified. The variables `a`, `x`, and `dx` are overwritten in each iteration, and their final values will be those from the last test case.

