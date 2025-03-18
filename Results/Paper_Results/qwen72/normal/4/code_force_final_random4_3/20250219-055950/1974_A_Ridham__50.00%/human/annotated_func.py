#State of the program right berfore the function call: The function should take two integers x and y as input, where 0 <= x, y <= 99, representing the number of applications with a 1x1 icon and the number of applications with a 2x2 icon, respectively.
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
        
    #State: `n` is 0, `result` is a list containing the calculated number of screens required for each iteration. `x` and `y` are integers where 0 <= `x`, `y` <= 99, `space_x` is equal to `x`, `space_y` is equal to `y * 4`, `total_space` is equal to `x + y * 4`. For each iteration, if `y` is even, `screen_require_for_y` is `y // 2`; if `y` is odd, `screen_require_for_y` is `y // 2 + 1`. `remaining_cells` is `15 * screen_require_for_y - space_y`. If `space_x` is less than or equal to `remaining_cells`, the value of `screen_require_for_y` is appended to `result`. Otherwise, `extra_screen` is calculated as `x // 15` if `space_x` is a multiple of 15, or `(x - remaining_cells) // 15 + 1` if `space_x` is not a multiple of 15, and `extra_screen + screen_require_for_y` is appended to `result`.
    print('\n'.join(map(str, result)))
    #This is printed: \n.join(map(str, result)) (where result is a list of integers representing the number of screens required for each iteration based on the given logic)
#Overall this is what the function does:The function `func` reads an integer `n` from the user, representing the number of test cases. For each test case, it reads two integers `x` and `y` from the user, where `0 <= x, y <= 99`. These integers represent the number of applications with 1x1 and 2x2 icons, respectively. The function calculates the minimum number of screens required to fit all the icons, assuming each screen can hold up to 15 cells (3x5 grid). The result for each test case is appended to a list `result`. After processing all test cases, the function prints each element of `result` on a new line. The final state of the program is that `n` is 0, `result` contains the calculated number of screens for each test case, and `x` and `y` are the last input values for the last test case.

