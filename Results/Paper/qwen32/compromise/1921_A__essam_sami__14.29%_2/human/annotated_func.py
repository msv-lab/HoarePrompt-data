#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, there are four pairs of integers (x_i, y_i) where -1000 ≤ x_i, y_i ≤ 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: The loop will have printed `t` lines, each line containing the smaller of the two calculated squared distances for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It then calculates the squared distances between two pairs of opposite corners and prints the smaller of the two squared distances for each test case.

