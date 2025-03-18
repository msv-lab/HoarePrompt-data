#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases where each test case contains an integer n (1 ≤ n ≤ 20). The function should generate a 2n × 2n checkerboard pattern as described.
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
        
    #State: The loop has finished executing all iterations, and the output for each test case (based on the value of `n` for each iteration) has been printed to the console. The variable `casos` remains unchanged, and the variable `n` will hold the value of the last input integer read during the last iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `casos` from the input, which indicates the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 20) and prints a 2n × 2n checkerboard pattern to the console. If `n` is outside the range of 1 to 4, it prints 'No esta en el rango'. After processing all test cases, the function does not return any value, but the checkerboard patterns or the out-of-range message for each test case have been printed to the console. The variable `casos` remains unchanged, and the variable `n` will hold the value of the last input integer read during the last iteration of the loop.

