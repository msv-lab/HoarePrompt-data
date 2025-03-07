#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 10, representing the size of the grid. Each grid is represented by n lines of n characters, where each character is either '0' or '1'. The grid contains exactly one triangle or one square that includes all the '1's, and the shape cannot consist of exactly one '1'.
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
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 100, `i` is `t-1`, `n` is the last input integer, `j` is `n-1`. If `a` is 'TRIANGLE', it means that at least one input string `s` had exactly one '1' in the last iteration. If `a` is 0, it means no input string `s` had exactly one '1' in the last iteration. `b` is 'SQUARE' if any input string `s` had more than one '1' in the last iteration; otherwise, `b` is an empty string.
#Overall this is what the function does:The function processes a series of test cases, each containing a grid of characters ('0' or '1'). For each test case, it determines and prints whether the grid represents a "TRIANGLE" or a "SQUARE" based on the pattern of '1's. A "TRIANGLE" is identified if any row in the grid has exactly one '1', while a "SQUARE" is identified if any row has more than one '1'. If no row has exactly one '1', the function defaults to printing "SQUARE". After processing all test cases, the function completes without returning any value.

