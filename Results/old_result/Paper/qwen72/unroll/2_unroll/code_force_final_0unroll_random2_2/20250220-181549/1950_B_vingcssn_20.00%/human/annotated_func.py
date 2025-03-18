#State of the program right berfore the function call: The function `func` is expected to read input from stdin, where the first line contains an integer t (1 ≤ t ≤ 20) representing the number of test cases, and each of the following t lines contains a single integer n (1 ≤ n ≤ 20) representing the size of the checkerboard to be generated.
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
        
    #State: The loop has finished executing all `t` iterations, and the checkerboard patterns for each `n` value have been printed to the console. The variable `casos` remains equal to `t`.
#Overall this is what the function does:The function `func` reads the number of test cases `t` from standard input, where `1 ≤ t ≤ 20`. For each test case, it reads an integer `n` (1 ≤ n ≤ 20) representing the size of a checkerboard to be generated. The function then prints a specific checkerboard pattern to the console based on the value of `n`. If `n` is 1, it prints a 2x2 checkerboard. If `n` is 2, it prints a 4x4 checkerboard. If `n` is 3, it prints a 6x6 checkerboard. If `n` is 4, it prints an 8x8 checkerboard. If `n` is outside the range of 1 to 4, it prints 'No esta en el rango'. After processing all test cases, the function completes and the variable `casos` remains equal to `t`. The function does not return any value.

