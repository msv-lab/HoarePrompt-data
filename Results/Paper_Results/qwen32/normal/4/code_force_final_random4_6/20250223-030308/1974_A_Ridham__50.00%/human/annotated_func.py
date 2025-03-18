#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, there are two integers x and y such that 0 <= x, y <= 99.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is 0, `x` and `y` are integers read from the input such that 0 <= x, y <= 99, `space_x` is equal to `x * 1`, `space_y` is equal to `y * 4`, `total_space` is equal to `space_y + space_x`. If `y` is even, `screen_require_for_y` is `y // 2`; otherwise, `screen_require_for_y` is `y // 2 + 1`. `remaining_cells` is calculated as `15 * screen_require_for_y - space_y`. If `space_x` is less than or equal to `remaining_cells`, `result` is a list containing the value of `screen_require_for_y`. Otherwise, `result` is a list containing one element, which is `extra_screen + screen_require_for_y`, where `extra_space` is `space_x - remaining_cells`, and `extra_screen` is `extra_space // 15 + 1` if `space_x` is not a multiple of 15, or `space_x // 15` if `space_x` is a multiple of 15. The loop has finished executing all iterations, and `result` contains the values determined for each iteration.
    print('\n'.join(map(str, result)))
    #This is printed: [screen_require_for_y or (extra_screen + screen_require_for_y) for each test case]
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers `x` and `y`. For each test case, it calculates the number of screens required to accommodate both `x` and `y` under specific conditions, and outputs the result for each test case.

