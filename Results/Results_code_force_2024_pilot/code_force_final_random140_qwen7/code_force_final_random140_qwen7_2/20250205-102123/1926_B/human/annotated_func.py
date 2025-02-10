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
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        
        if a != 0:
            print(a)
        else:
            print(b)
        
    #State: t must be greater than 0, i is 3, a is either 'Triangle', 'Square', or 0, b is 'Square', j is equal to `n` + 1, `n` is greater than or equal to the number of times the loop executed (which is `t`), and `s` is the last input string received during the loop's execution.
#Overall this is what the function does:The function processes multiple grids, each defined by an integer \( n \) and a list of \( n \) strings, where each string contains \( n \) characters ('0' or '1'). It identifies whether the grid contains a triangle or a square that includes all '1's and has a size greater than 1. If a triangle is found, it prints 'Triangle'; otherwise, it prints 'Square'. The function does not return any value but prints the identified shape for each grid.

