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
        
    #State: Output State: `casos` must be greater than 0, `t` is an integer such that \(1 \leq t \leq 20\), `n` is an integer input by the user for each iteration of the loop, `c` is equal to `casos - 1`.
    #
    #This means that after the loop has executed all its iterations, `casos` will have been decremented by the number of times the loop ran, leaving `c` as `casos - 1`. The value of `n` will depend on the input provided during each iteration of the loop. The variable `t` remains unchanged as it is not affected by the loop.
#Overall this is what the function does:The function reads a number of test cases and for each case, it reads an integer \(n\) and prints a specific pattern based on the value of \(n\). If \(n\) is 1, it prints two lines of "##". If \(n\) is 2, it prints four lines with alternating patterns. If \(n\) is 3, it prints six lines with a more complex pattern. If \(n\) is 4, it prints eight lines with an even more complex pattern. If \(n\) is outside the range 1 to 4, it prints "No esta en el rango". After processing all test cases, the function outputs the final value of `c`, which is `casos - 1`.

