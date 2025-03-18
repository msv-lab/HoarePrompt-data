#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, with the size of the triangle or square being greater than 1.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, and for each iteration of the outer loop, if any string `s` has exactly one '1', the output is 'TRIANGLE', otherwise, the output is 'SQUARE'.
#Overall this is what the function does:The function processes multiple grids (up to 100 grids) where each grid is defined by n lines of n characters ('0' or '1'). It checks each grid to determine if it contains a shape (either a triangle or a square) that includes all the '1's in the grid. If any line in the grid contains exactly one '1', it outputs 'TRIANGLE'. Otherwise, it outputs 'SQUARE'.

