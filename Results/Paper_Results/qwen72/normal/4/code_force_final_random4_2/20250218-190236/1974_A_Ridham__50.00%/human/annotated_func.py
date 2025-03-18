#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, x and y are integers such that 0 <= x, y <= 99.
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
            if space_x % 15 == 0:
                extra_screen = space_x // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: `n` is 0, `_` is a placeholder, `x` and `y` are integers provided by the user input, `space_x` is equal to the last value of `x`, `space_y` is equal to the last value of `y * 4`, `total_space` is equal to the last value of `space_x + space_y`, `screen_require_for_y` is equal to the last value of `y // 2` if `y` is even or `y // 2 + 1` if `y` is odd, `remaining_cells` is equal to the last value of `15 * screen_require_for_y - y * 4`. If the last value of `space_x` is less than or equal to the last value of `remaining_cells`, `result` is a list that includes the value of `screen_require_for_y` for each iteration. Otherwise, `result` is a list that includes the value of `extra_screen + screen_require_for_y` for each iteration, where `extra_screen` is equal to `space_x // 15` if `space_x` is a multiple of 15, or `space_x // 15 + 1` if `space_x` is not a multiple of 15, and `extra_space` is equal to the last value of `space_x - remaining_cells`.
    print('\n'.join(map(str, result)))
    #This is printed: 3
    #3
    #3
    #...
#Overall this is what the function does:The function `func` reads an integer `n` from user input, indicating the number of test cases. For each test case, it reads two integers `x` and `y` from user input. It calculates the number of screens required to accommodate `x` units of space and `y` units of space, where each unit of `y` requires 4 cells and each screen can hold up to 15 cells. If the space required for `x` can be accommodated within the remaining cells after placing `y`, it appends the number of screens required for `y` to the result list. Otherwise, it calculates the additional screens needed for the remaining `x` space and appends the total number of screens to the result list. Finally, it prints each element of the result list on a new line.

