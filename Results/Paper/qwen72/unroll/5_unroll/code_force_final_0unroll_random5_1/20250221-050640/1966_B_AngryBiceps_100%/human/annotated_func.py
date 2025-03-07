#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n and m are integers such that 1 <= n, m <= 500, and the grid is a list of n strings, each of length m, containing characters 'W' and 'B'.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        a = []
        
        first_row = ''
        
        last_row = ''
        
        for i in range(n):
            a.append(input())
            first_row += a[-1][0]
            last_row += a[-1][-1]
        
        if len(set(a[0])) == 1 and len(set(a[-1])) == 1 and a[0] != a[-1]:
            print('NO')
        elif len(set(first_row)) == 1 and len(set(last_row)
            ) == 1 and first_row != last_row:
            print('NO')
        else:
            print('YES')
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` and `m` from input, constructs a grid `a` of `n` strings each of length `m`, and checks certain conditions on the grid. After all iterations, `t` is unchanged, and `n`, `m`, and `a` are not retained between iterations. The variables `first_row` and `last_row` are reset for each iteration. The output state is the same as the initial state, except that the loop has been executed `t` times, and the program has printed 'YES' or 'NO' for each grid based on the conditions checked.
#Overall this is what the function does:The function `func` reads an integer `t` and then iterates `t` times. In each iteration, it reads two integers `n` and `m`, and a grid of `n` strings, each of length `m`, containing characters 'W' and 'B'. The function checks if the first and last rows of the grid, as well as the first and last characters of each row, meet certain conditions. If any of these conditions are not met, it prints 'NO'; otherwise, it prints 'YES'. After all iterations, the function has printed 'YES' or 'NO' for each grid, and the state of the program is the same as before the function call, except for the output produced.

