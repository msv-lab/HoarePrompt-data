#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case includes an integer `n` (2 ≤ n ≤ 10) representing the size of the grid, and a list of `n` strings, each string containing `n` characters of '0' or '1'. The grid contains exactly one triangle or one square, and the shape's size is greater than 1.
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
        
    #State: The loop will print 'TRIANGLE' or 'SQUARE' for each test case based on the shape found in the grid. The variable `a` will be set to 'TRIANGLE' if a triangle is found, and `b` will be set to 'SQUARE' if a square is found. After all iterations, the values of `t` and `n` will remain unchanged, and `a` and `b` will be reset for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case includes an integer `n` (2 ≤ n ≤ 10) representing the size of a grid, followed by `n` strings, each containing `n` characters ('0' or '1'). The function prints 'TRIANGLE' if any row in the grid contains exactly one '1', and 'SQUARE' if any row contains more than one '1'. If no row contains a '1', it prints 'SQUARE'. The function does not return any value. After processing all test cases, the variables `t` and `n` remain unchanged, and the variables `a` and `b` are reset for each test case.

