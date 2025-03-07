#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is an integer such that 1 ≤ t ≤ 20. For each iteration, an integer n is provided such that 1 ≤ n ≤ 20.
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
        
    #State: The loop will execute `casos` times, and for each iteration, it will print a pattern based on the value of `n` provided. If `n` is 1, it will print two lines of '##'. If `n` is 2, it will print four lines of '##..' followed by four lines of '..##'. If `n` is 3, it will print six lines of '##..##' followed by six lines of '..##..'. If `n` is 4, it will print eight lines of '##..##..' followed by eight lines of '..##..##'. If `n` is outside the range 1 to 4, it will print 'No esta en el rango'. The value of `c` will be `casos - 1` after the loop finishes, and the value of `n` will be the last input provided. The value of `casos` remains unchanged.
#Overall this is what the function does:The function `func` is designed to be called within a loop that iterates `t` times, where `t` is an integer between 1 and 20. For each iteration, the function reads an integer `n` from the user input, where 1 ≤ n ≤ 20. The function prints a specific pattern of '##' and '.' characters based on the value of `n`. If `n` is 1, it prints two lines of '##'. If `n` is 2, it prints four lines of '##..' followed by four lines of '..##'. If `n` is 3, it prints six lines of '##..##' followed by six lines of '..##..'. If `n` is 4, it prints eight lines of '##..##..' followed by eight lines of '..##..##'. If `n` is outside the range 1 to 4, it prints 'No esta en el rango'. The function does not return any value. After the function concludes, the value of `casos` remains unchanged, and the value of `n` will be the last input provided.

