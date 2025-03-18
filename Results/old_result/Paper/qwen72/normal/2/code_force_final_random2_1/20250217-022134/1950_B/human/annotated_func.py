#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 20, and for each test case, n is an integer where 1 ≤ n ≤ 20.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 20, `casos` must be equal to the initial value of `casos`, `c` is `casos - 1`, and `n` is an input integer where 1 ≤ n ≤ 20. The value of `n` remains unchanged for each iteration based on the input provided.
#Overall this is what the function does:The function `func` reads an integer `casos` indicating the number of test cases, where `1 ≤ casos ≤ 20`. For each test case, it reads another integer `n` (where `1 ≤ n ≤ 20`) and prints a pattern of `#` and `.` characters based on the value of `n`. If `n` is 1, it prints a 2x2 grid of `##`. If `n` is 2, it prints a 4x4 grid with a specific pattern. If `n` is 3, it prints a 6x6 grid with a specific pattern. If `n` is 4, it prints an 8x8 grid with a specific pattern. If `n` is outside the range of 1 to 4, it prints 'No esta en el rango'. After processing all test cases, the function completes without returning any value. The final state of the program is that `casos` remains unchanged, and `n` retains its last input value for each test case.

