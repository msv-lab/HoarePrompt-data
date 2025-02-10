#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100; for each test case, n is an integer such that 2 ≤ n ≤ 10; the grid is represented as a list of n strings, each string contains n characters which are either '0' or '1', and the grid contains exactly one triangle or exactly one square that includes all the '1's in the grid.
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
        
    #State: All iterations of the loop have finished, with `i` being equal to `t`, `t` being the total number of times the loop ran, `n` being the total number of inputs received during the last iteration, `a` being 'Triangle' if any of the input strings had exactly one '1', and 'Square' if all input strings had more than one '1', and `b` being 'Square' if any of the input strings had more than one '1', and remaining an empty string if no such string was entered.
#Overall this is what the function does:The function processes a series of grids, each represented as a list of n strings containing '0's and '1's. It determines whether the shape formed by '1's in each grid is a triangle or a square. If any row in the grid contains exactly one '1', it prints 'Triangle'. Otherwise, it prints 'Square'. The function runs this check for each of the t test cases provided. After processing all test cases, it outputs the determined shape for each grid.

