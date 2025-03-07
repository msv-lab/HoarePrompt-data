#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: The final state of the loop will have `t` remaining as a positive integer such that 1 ≤ t ≤ 10^4, `result` will be a list containing the sum of `screen_require_for_y` and `extra_screen` for each iteration where `space_x` exceeds `remaining_cells`, and `x` and `y` will be the last integers provided by the input split during the last iteration of the loop.
    print('\n'.join(map(str, result)))
    #This is printed: a list of sums (each sum is screen_require_for_y + extra_screen for each iteration where space_x > remaining_cells), each sum on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and pairs of non-negative integers `x` and `y`. For each pair, it calculates a value based on the relationship between `x`, `y`, and certain derived values like `space_x`, `space_y`, and `remaining_cells`. If `space_x` is less than or equal to `remaining_cells`, it appends `screen_require_for_y` to the result list. Otherwise, it calculates `extra_screen` and appends the sum of `extra_screen` and `screen_require_for_y` to the result list. Finally, it prints a list of these calculated values, one per line.

