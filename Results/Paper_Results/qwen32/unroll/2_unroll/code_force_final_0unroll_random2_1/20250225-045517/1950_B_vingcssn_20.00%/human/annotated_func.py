#State of the program right berfore the function call: t is an integer such that 1 <= t <= 20, and for each test case, n is an integer such that 1 <= n <= 20.
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
        
    #State: t is an integer such that 1 <= t <= 20, n is 3, casos is an integer such that 1 <= casos <= 20.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where 1 <= `t` <= 20. For each test case, it reads an integer `n` such that 1 <= `n` <= 20. It then prints a pattern of `n` by `n` blocks separated by dots, with each block being 2x2 characters. If `n` is not within the range 1 to 4, it prints 'No esta en el rango'.

