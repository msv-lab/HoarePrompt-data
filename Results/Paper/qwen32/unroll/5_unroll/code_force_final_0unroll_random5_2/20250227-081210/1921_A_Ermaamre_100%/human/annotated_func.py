#State of the program right berfore the function call: The input consists of several test cases. The first line contains an integer t (1 ≤ t ≤ 100), representing the number of test cases. Each test case consists of four lines, with each line containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000), representing the coordinates of the corners of a square. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The output state consists of `t` lines, each containing the area of the square formed by the coordinates provided in the corresponding test case.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. For each test case, it calculates and prints the area of the square.

