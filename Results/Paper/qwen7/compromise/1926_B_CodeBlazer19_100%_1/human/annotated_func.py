#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the input consists of n lines, each containing n characters that are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid.
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
        
    #State: Postcondition: `t` must be greater than 0, `i` is equal to `t`, `a` is 'TRIANGLE', `b` is 'SQUARE', `j` is `n + t - 1`, `n` is the sum of all individual `n` values input during each iteration, and `s` is the final input string from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of '0's and '1's. For each grid, it determines whether the '1's form a triangle or a square. If a single row contains exactly one '1', it concludes the shape is a triangle; otherwise, it concludes the shape is a square. The function prints 'TRIANGLE' or 'SQUARE' for each test case.

