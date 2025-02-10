#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines, each containing n characters ('0' or '1'). The grid contains exactly one triangle or exactly one square that includes all the '1's in the grid, and the shape cannot consist of exactly one '1'.
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
        
    #State: `t` is an integer between 1 and 100 (inclusive), `i` is `t-1`, `n` is the last input integer, `j` is `n-1`, and `s` is the last input string. For each test case, if any input string contained exactly one '1', `a` is set to 'Triangle'. If any input string contained more than one '1', `b` is set to 'Square'. If no input string contained exactly one '1' or more than one '1', `a` remains 0 and `b` remains an empty string. If `a` is not 0, `b` remains an empty string if no input string contained more than one '1', otherwise, `b` is set to 'Square'. If `a` is 0, `a` remains 0.
#Overall this is what the function does:The function reads multiple test cases, each involving a grid of '0's and '1's. For each test case, it determines and prints whether the grid contains a shape (either a triangle or a square) that includes all the '1's. Specifically, if any row in the grid contains exactly one '1', it prints 'Triangle'. If any row contains more than one '1', it prints 'Square'. If no row contains exactly one '1' or more than one '1', it defaults to printing 'Square'. The function processes up to 100 test cases, with each grid being up to 10x10 in size.

