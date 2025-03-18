#State of the program right berfore the function call: The function should take a list of tuples as input, where each tuple contains the coordinates (x, y) of a corner of the square, and the list contains exactly four tuples. The coordinates x_i and y_i are integers such that -1000 <= x_i, y_i <= 1000. The input list represents the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop will print the smaller of the squared distances between the pairs of points (a, b) and (e, f), and (c, d) and (g, h), for each iteration of the loop. The values of `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, and `t` will remain unchanged after the loop finishes executing.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads four pairs of integers (coordinates) from the input. It then calculates the squared distances between two pairs of points: (a, b) and (e, f), and (c, d) and (g, h). The function prints the smaller of these two squared distances for each test case. The function does not return any value and does not modify the input variables.

