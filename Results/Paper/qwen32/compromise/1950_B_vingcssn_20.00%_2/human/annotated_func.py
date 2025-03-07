#State of the program right berfore the function call: t is an integer such that 1 <= t <= 20, and for each of the t test cases, n is an integer such that 1 <= n <= 20.
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
        
    #State: - The value of `t` and `casos` remains unchanged.
    #   - The loop will execute `t` times, and for each iteration, it will print a pattern based on the value of `n` read from the input.
    #   - The state of the variables `t` and `casos` is not altered by the loop.
    #
    #Given the above, the output state can be described as follows:
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints a specific pattern based on the value of `n`. If `n` is 1, 2, 3, or 4, it prints predefined patterns. For any other value of `n`, it prints 'No esta en el rango'.

