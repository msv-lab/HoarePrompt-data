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
        
    #State: After the loop executes all its iterations, `i` will be equal to `t`, which is the total number of iterations the loop was supposed to run. The variable `a` will be 'TRIANGLE' if at least one of the input strings contained exactly one '1'. Otherwise, `a` will be 0. The variable `b` will be 'SQUARE' if any of the input strings contained more than one '1'. If no input string contained exactly one '1' or more than one '1', `b` will remain its last assigned value, which could be 'TRIANGLE' or 'SQUARE'. The variable `j` will be equal to `n - 1` for the last iteration, but since the loop has completed, `j` will not be incremented further. The variable `s` will hold the last input string processed by the loop.
#Overall this is what the function does:The function processes multiple test cases, each involving a grid of '0's and '1's with dimensions n x n (where 2 ≤ n ≤ 10). For each test case, it checks if the '1's form a triangle or a square. If at least one row contains exactly one '1', it prints 'TRIANGLE'. If any row contains more than one '1', it prints 'SQUARE'. If neither condition is met, it prints the last determined shape type (which could be 'TRIANGLE' or 'SQUARE').

