#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each of the t test cases, there are four pairs of integers (x_i, y_i) where -1000 <= x_i, y_i <= 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: `t` is the integer input, where 0 < `t` <= 100; the loop has executed `t` times, and for each iteration, a 2D list `a` containing 4 sublists of integers from input lines has been processed. `x` is a list containing the first element of each of the 4 sublists in the current `a`, and `dx` is the difference between the maximum and minimum values in `x`. The loop prints `dx * dx` for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It then calculates and prints the area of each square.

