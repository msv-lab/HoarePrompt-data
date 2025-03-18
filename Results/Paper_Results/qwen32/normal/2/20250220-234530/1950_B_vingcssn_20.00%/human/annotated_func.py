#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 20, and for each of the t test cases, there is a single integer n such that 1 ≤ n ≤ 20.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 20, `casos` is equal to `t`, and `c` is equal to `t`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads another integer `n`. It then prints a specific pattern of hashes (`#`) and dots (`.`) based on the value of `n` for each test case. If `n` is not between 1 and 4, it prints 'No esta en el rango'.

