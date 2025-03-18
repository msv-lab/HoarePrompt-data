#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines, each containing n characters ('0' or '1'). The grid contains exactly one triangle or exactly one square that includes all the '1's, and the shape's size is greater than 1.
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
        
    #State: `t` is an integer input by the user, 1 ≤ t ≤ 100; `i` is `t-1`; `n` is the last integer input by the user; `j` is `n-1`. If any of the input strings `s` for any test case contained exactly one '1', `a` is 'TRIANGLE'. Otherwise, `a` is 0. If any of the input strings `s` for any test case contained more than one '1', `b` is 'SQUARE'. Otherwise, `b` remains an empty string.
#Overall this is what the function does:The function `func` reads a series of test cases from the input. Each test case consists of an integer `n` followed by an `n x n` grid represented by `n` lines of `n` characters ('0' or '1'). The function determines whether the grid contains a triangle or a square based on the pattern of '1's. If any row in the grid contains exactly one '1', the function prints 'TRIANGLE'. If any row contains more than one '1', the function prints 'SQUARE'. If no row meets either condition, the function prints 'SQUARE'. After processing all test cases, the function completes, and the final state is that the input has been fully read and processed, and the appropriate shape (triangle or square) has been printed for each test case.

