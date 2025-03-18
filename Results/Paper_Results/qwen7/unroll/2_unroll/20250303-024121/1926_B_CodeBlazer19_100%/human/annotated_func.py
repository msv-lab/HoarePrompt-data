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
                a = 'TRIANGLE'
            elif s.count('1') > 1:
                b = 'SQUARE'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, and for each i in range(t), either 'TRIANGLE' or 'SQUARE' is printed based on the input strings s. If any string s has exactly one '1', 'TRIANGLE' is printed; otherwise, 'SQUARE' is printed for that particular i.
#Overall this is what the function does:The function processes a series of grids, each represented as a list of n strings containing '0's and '1's. It determines whether each grid contains a single triangle or a single square that includes all '1's. Based on this determination, it prints either 'TRIANGLE' or 'SQUARE' for each grid. If any row in a grid has exactly one '1', it prints 'TRIANGLE'; otherwise, it prints 'SQUARE'.

