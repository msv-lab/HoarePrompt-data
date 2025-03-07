#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. Each of the following t test cases consists of four lines, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive (strictly greater than 0) area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The variable `t` remains unchanged, and for each test case, the program outputs the square of the difference between the maximum and minimum of the first elements of four input lists.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It then calculates and prints the area of each square.

