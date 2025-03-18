#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) representing the number of test cases, followed by t sets of four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. The coordinates are given in random order, but it is guaranteed that they form a square with sides parallel to the coordinate axes and with a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: `t` must be greater than 0, `_` is `t-1`, `a` is a 4xN list of integers where N is the number of integers input on each line, `x` is a list containing the first element of each sublist in `a`, `dx` is the difference between the maximum and minimum values in `x`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers `x_i`, `_y_i_` representing the coordinates of the corners of a square. The function then calculates the side length of the square by finding the difference between the maximum and minimum x-coordinates and prints the area of the square (side length squared) for each test case. The function does not return any values; it only prints the areas of the squares.

