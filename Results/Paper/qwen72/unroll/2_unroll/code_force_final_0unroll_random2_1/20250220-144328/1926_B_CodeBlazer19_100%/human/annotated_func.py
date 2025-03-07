#State of the program right berfore the function call: The function should accept a 2D list `grid` of size n x n where each element is either '0' or '1', and n is an integer such that 2 ≤ n ≤ 10. The grid contains exactly one triangle or one square that includes all the '1's, and the shape size is greater than 1.
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
        
    #State: The function will print 'TRIANGLE' or 'SQUARE' for each iteration of the loop based on the input grid. The variables `a` and `b` will be reset to their initial values (`a = 0` and `b = ''`) at the start of each iteration. After all iterations, the final values of `a` and `b` will be `0` and `''` respectively, and the variable `t` will remain unchanged.
#Overall this is what the function does:The function `func` reads multiple 2D grids from user input, where each grid is of size n x n (2 ≤ n ≤ 10) and contains elements '0' or '1'. For each grid, it determines and prints whether the shape formed by the '1's is a "TRIANGLE" or a "SQUARE". The function does not return any value. After processing all grids, the variables `a` and `b` are reset to their initial values (`a = 0` and `b = ''`) at the start of each iteration, and the variable `t` (the number of grids) remains unchanged.

