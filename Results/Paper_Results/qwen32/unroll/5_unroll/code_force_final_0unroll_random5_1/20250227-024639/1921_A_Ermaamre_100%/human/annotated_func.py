#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, there are four pairs of integers (x_i, y_i) where -1000 <= x_i, y_i <= 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: a series of t printed numbers, each representing the area of a square from the corresponding test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It calculates and prints the area of each square.

