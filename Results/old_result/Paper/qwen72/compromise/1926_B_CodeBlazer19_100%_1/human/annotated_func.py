#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines, each containing n characters, either '0' or '1'. The grid contains exactly one triangle or one square that includes all the '1's, and the shape's size is greater than 1.
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
        
    #State: `t` is 0, `i` is `t-1`, `n` is the last input integer, `j` is `n-1`, and `s` is the last input string provided by the user. If any input string `s` contains exactly one '1' character, `a` is set to 'TRIANGLE'. If any input string `s` contains more than one '1' character, `b` is set to 'SQUARE'. If no input string `s` contains exactly one '1', `a` is 0. If no input string `s` contains more than one '1', `b` remains an empty string.
#Overall this is what the function does:The function reads a series of test cases, each consisting of an integer `n` and an `n x n` grid of characters ('0' or '1'). For each test case, it determines whether the grid contains a shape (triangle or square) that includes all the '1's. If any row in the grid contains exactly one '1', it prints 'TRIANGLE'. If any row contains more than one '1', it prints 'SQUARE'. If no row contains exactly one '1', it defaults to printing 'SQUARE'. After processing all test cases, the function completes without returning any value.

