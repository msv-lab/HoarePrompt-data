#State of the program right berfore the function call: The function should accept two parameters, x and y, where x and y are non-negative integers such that 0 <= x, y <= 99.
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
        
    #State: `x` and `y` are non-negative integers such that 0 <= x, y <= 99, `n` is an input integer, `result` is a list containing the number of screens required for each iteration of the loop, where the number of screens required for each iteration is calculated as follows: If `y` is even, `screen_require_for_y` is `y // 2`, and if `y` is odd, `screen_require_for_y` is `y // 2 + 1`. The remaining cells on the screen are calculated as `15 * screen_require_for_y - y * 4`. If `space_x` (which is `x`) is less than or equal to `remaining_cells`, the number of screens required for that iteration is `screen_require_for_y`. Otherwise, the number of screens required is `extra_screen + screen_require_for_y`, where `extra_space` is `x - remaining_cells`, and `extra_screen` is `extra_space // 15` if `extra_space % 15 == 0` or `extra_space // 15 + 1` otherwise.
    print('\n'.join(map(str, result)))
    #This is printed: 5
    #8
    #10
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. Instead, it reads an integer `n` from the user input, indicating the number of iterations. For each iteration, it reads two non-negative integers `x` and `y` (where 0 <= x, y <= 99) from the user input. The function calculates the number of screens required based on the values of `x` and `y`. Specifically, it determines the number of screens needed for `y` (even or odd) and checks if `x` can fit into the remaining cells on those screens. If `x` fits, the number of screens required is the same as for `y`. If `x` does not fit, additional screens are calculated based on the remaining space needed for `x`. The function then prints the number of screens required for each iteration, one per line.

