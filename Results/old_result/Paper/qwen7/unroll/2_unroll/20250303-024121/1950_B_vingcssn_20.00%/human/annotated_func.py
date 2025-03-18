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
        
    #State: Output State: The output will consist of multiple patterns printed based on the value of `n` for each iteration of the loop. If `n` is 1, two lines of "##" will be printed. If `n` is 2, four lines of specific patterns will be printed. If `n` is 3, six lines of specific patterns will be printed. If `n` is 4, eight lines of specific patterns will be printed. If `n` is greater than 4, the message "No esta en el rango" (which means "Not in the range") will be printed for each case outside the specified range. The total number of these patterns will depend on the value of `casos`, which is the number of times the loop runs.
#Overall this is what the function does:The function reads an integer `casos` indicating the number of test cases. For each test case, it reads an integer `n`. Depending on the value of `n`, it prints a specific pattern consisting of "#" and "." characters. If `n` is 1, it prints two lines of "##". If `n` is 2, it prints four lines with specific patterns. If `n` is 3, it prints six lines with specific patterns. If `n` is 4, it prints eight lines with specific patterns. If `n` is greater than 4, it prints "No esta en el rango" for each case. The function does not return anything and only outputs the patterns or the out-of-range message.

