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
        
    #State: Output State: After the loop executes all its iterations, the output state will be as follows: `c` is equal to `casos - 1`, `casos` retains its initial value (which is a positive integer greater than 0), and `n` retains its last input value. The loop prints patterns based on the value of `n` for each iteration, and these patterns are printed according to the conditions specified in the code. If `n` is outside the specified range (1 to 4), it prints "No esta en el rango" (which means "Not in the range" in Spanish).
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`. For each `n` within the range 1 to 4, it prints a specific pattern. If `n` is 1, it prints two lines of double hashes. If `n` is 2, it prints four lines with alternating double hashes and dots. If `n` is 3, it prints six lines with a more complex alternating pattern. If `n` is 4, it prints eight lines with an even more intricate pattern. If `n` is outside the range 1 to 4, it prints "No esta en el rango". After processing all test cases, the function does not return any value; it only outputs the patterns based on the input values.

