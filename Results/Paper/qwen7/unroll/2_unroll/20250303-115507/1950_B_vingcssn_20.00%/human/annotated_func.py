#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 20, and for each test case, n is an integer such that 1 ≤ n ≤ 20.
def func():
    casos = int(input())
    for c in range(0, casos):
        n = int(input())
        
        if n == 1:
            print('##')
            print('##')
        elif n == 2:
            print('##..')
            print('##..')
            print('..##')
            print('..##')
        elif n == 3:
            print('##..##')
            print('##..##')
            print('..##..')
            print('..##..')
            print('##..##')
            print('##..##')
        elif n == 4:
            print('##..##..')
            print('##..##..')
            print('..##..##')
            print('..##..##')
            print('##..##..')
            print('##..##..')
            print('..##..##')
            print('..##..##')
        else:
            print('No esta en el rango')
        
    #State: Output State: The output will consist of multiple sections, each corresponding to the value of `n` provided for each iteration of the loop. For each `n`, the output will display a specific pattern printed according to the conditions given in the loop. If `n` is outside the specified range (1 to 4), it will print "No esta en el rango" (which means "Not in the range") for that iteration. Each section of the output will be separated by blank lines.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n`. Based on the value of `n`, it prints a specific pattern consisting of `#` and `.` characters. If `n` is 1, it prints a 2x2 pattern; if `n` is 2, a 4x4 pattern; if `n` is 3, a 6x6 pattern; and if `n` is 4, an 8x8 pattern. If `n` is outside the range 1 to 4, it prints "No esta en el rango". After processing all test cases, it ends with no further output.

