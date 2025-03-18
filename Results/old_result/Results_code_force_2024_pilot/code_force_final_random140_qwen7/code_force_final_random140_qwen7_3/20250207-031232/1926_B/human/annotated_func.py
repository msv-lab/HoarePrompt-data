#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 2 ≤ n ≤ 10, and the grid is represented as a list of n strings, each string containing n characters that are either '0' or '1'. The grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the size of the triangle or square is greater than 1.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = 0
        
        b = ''
        
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: After the loop executes all iterations, `t` will be the total number of iterations the loop ran, `n` will be greater than 0 for each iteration, `a` will be 'Triangle' if any string `s` across all iterations contained exactly one '1', otherwise `a` will be 0, and `b` will be 'Square' because it gets set to 'Square' in every iteration regardless of the value of `s`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a grid represented as a list of n strings, where each string contains n binary characters ('0' or '1'). For each test case, it determines whether the grid contains a triangle or a square that includes all '1's and has a size greater than 1. If any row contains exactly one '1', it identifies the shape as a triangle; otherwise, it identifies the shape as a square. The function prints 'Triangle' if a triangle is found, and 'Square' if no triangle is found but a square is identified.

