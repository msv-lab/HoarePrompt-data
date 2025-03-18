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
        
    #State: Output State: The output will consist of multiple patterns printed based on the value of `n` for each iteration of the loop. If `n` is 1, it will print two lines with `##`. If `n` is 2, it will print four lines with `##..` followed by four lines with `..##`. If `n` is 3, it will print six lines with various combinations of `##` and `..`. If `n` is 4, it will print eight lines with specific patterns. If `n` is outside the range 1 to 4, it will print 'No esta en el rango' (which means 'Not in the range') for that iteration. The number of times each pattern is printed corresponds to the value of `casos`.
#Overall this is what the function does:Functionality: The function processes a series of test cases defined by the variable `casos`. For each test case, it reads an integer `n` and prints a specific pattern based on the value of `n`. If `n` is 1, it prints two lines of `##`. If `n` is 2, it prints four lines with alternating `##..` and `..##`. If `n` is 3, it prints six lines with a combination of `##` and `..`. If `n` is 4, it prints eight lines with a specific pattern. If `n` is outside the range 1 to 4, it prints 'No esta en el rango' for that iteration. After processing all test cases, the function concludes without returning any value.

