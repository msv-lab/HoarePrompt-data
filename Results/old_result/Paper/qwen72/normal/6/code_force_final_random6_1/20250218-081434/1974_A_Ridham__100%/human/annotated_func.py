#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x and y are integers such that 0 <= x, y <= 99.
def func():
    n = int(input())
    result = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        
        space_x = x * 1
        
        space_y = y * 4
        
        total_space = space_y + space_x
        
        if y % 2 == 0:
            screen_require_for_y = y // 2
        else:
            screen_require_for_y = y // 2 + 1
        
        remaining_cells = 15 * screen_require_for_y - space_y
        
        if space_x <= remaining_cells:
            result.append(screen_require_for_y)
        else:
            extra_space = space_x - remaining_cells
            if extra_space % 15 == 0:
                extra_screen = extra_space // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `x` and `y` are integers provided by the user input, `n` is the number of iterations the loop has executed, `result` is a list containing the number of screens required for each of the `n` test cases. For each test case, if `space_x` (which is `x`) is less than or equal to `remaining_cells` (which is `15 * screen_require_for_y - space_y`), `result` contains the value of `screen_require_for_y` (which is `y // 2` if `y` is even or `y // 2 + 1` if `y` is odd). If `space_x` is greater than `remaining_cells`, `result` contains the value `extra_screen + screen_require_for_y`, where `extra_space` is `space_x - remaining_cells` and `extra_screen` is `extra_space // 15` if `extra_space % 15 == 0` or `extra_space // 15 + 1` otherwise.
    print('\n'.join(map(str, result)))
    #This is printed: [screen_require_for_y or extra_screen + screen_require_for_y for each test case, one per line]
#Overall this is what the function does:The function `func` reads an integer `n` from user input, which represents the number of test cases. For each test case, it reads two integers `x` and `y` from user input. It calculates the number of screens required to accommodate `x` and `y` based on the following rules: `x` requires 1 unit of space, and `y` requires 4 units of space. If the space required for `x` can fit into the remaining cells after allocating space for `y` (where each screen can hold up to 15 units of space for `y`), the function appends the number of screens required for `y` to the result list. If not, it calculates the additional screens needed for the remaining space required by `x` and appends the total number of screens to the result list. Finally, the function prints the number of screens required for each test case, one per line.

