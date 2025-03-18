#State of the program right berfore the function call: The function should take a grid as input, where the grid is a list of strings, each string representing a row of the grid and consisting of characters '0' or '1'. The grid is of size n x n, where 2 ≤ n ≤ 10. The grid contains exactly one triangle or one square, and the shape cannot consist of exactly one '1'.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: The grid remains unchanged, and the loop prints either 'TRIANGLE' or 'SQUARE' for each iteration based on the input grid.
#Overall this is what the function does:The function reads a series of grids from user input, where each grid is a list of strings representing a grid of size n x n (2 ≤ n ≤ 10) with characters '0' or '1'. For each grid, it prints 'TRIANGLE' if any row contains exactly one '1', and 'SQUARE' if any row contains more than one '1'. If no row contains a '1', it prints 'SQUARE'. The function does not modify the input grids.

