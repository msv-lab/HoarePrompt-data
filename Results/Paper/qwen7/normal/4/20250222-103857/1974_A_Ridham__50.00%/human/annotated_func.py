#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: The loop has executed all its iterations, and `result` is a list containing the sum of `screen_require_for_y` and `extra_screen` for each iteration where `space_x` was greater than `remaining_cells`. For each iteration, `space_x` is set to `x * 1` and `space_y` is set to `y * 4`. If `space_x` is less than or equal to `remaining_cells`, `screen_require_for_y` is added to `result`. Otherwise, `extra_screen + screen_require_for_y` is added to `result`, where `extra_screen` is either `space_x // 15` if `space_x` is divisible by 15, or `space_x // 15 + 1` otherwise. The final state of `t`, `n`, `total_space`, `x`, `y`, `space_x`, `space_y`, `screen_require_for_y`, `remaining_cells`, and `extra_space` remains as defined in the precondition.
    #
    #In simpler terms, after all iterations, `result` will contain the sum of `screen_require_for_y` and `extra_screen` for each input pair `(x, y)` where `space_x` was not enough to meet `remaining_cells`. `t` and `n` will reflect the initial conditions and the number of inputs processed, respectively.
    print('\n'.join(map(str, result)))
    #This is printed: the elements of the `result` list, each on a new line
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 10^4. For each test case, it takes two integers `x` and `y` (both between 0 and 99) as input. Based on these values, it calculates the required screen space and any additional space needed. The function then constructs a list `result` containing the sum of the required screen space and any additional space for each test case where the available space (`space_x`) is insufficient to meet the required space (`remaining_cells`). Finally, it prints each element of the `result` list on a new line.

