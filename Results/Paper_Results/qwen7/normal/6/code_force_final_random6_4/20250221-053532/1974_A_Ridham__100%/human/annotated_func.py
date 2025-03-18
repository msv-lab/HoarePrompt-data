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
            if extra_space % 15 == 0:
                extra_screen = extra_space // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: Output State: The loop will execute `n` times, where `n` is the input integer provided at the start. After all iterations, `result` will be a list containing the number of elements that satisfy the conditions specified within the loop. Each element in the list represents the value of `screen_require_for_y` or `extra_screen + screen_require_for_y` based on the conditions met during each iteration.
    #
    #- `remaining_cells` will be recalculated for each iteration based on the current values of `y` and `space_y`.
    #- `space_x` will remain constant as it is initialized to `x * 1` and does not change throughout the loop.
    #- `space_y` will be updated to `y * 4` for each new iteration.
    #- `total_space` will be the sum of `space_y` and `space_x`.
    #- `t` and `n` will retain their initial values since they are not modified within the loop.
    #- `x` and `y` will be updated with new input values for each iteration.
    #- `screen_require_for_y` will be either `y // 2` or `y // 2 + 1` based on whether `y` is even or odd.
    #- `extra_space` will be `space_x - remaining_cells`.
    #- `extra_screen` will be calculated as `extra_space // 15 + 1` if `extra_space % 15 != 0`, or `extra_space // 15` otherwise.
    #
    #The final `result` list will contain the outcomes of each iteration, either `screen_require_for_y` or `extra_screen + screen_require_for_y`, depending on the conditions evaluated in the loop.
    print('\n'.join(map(str, result)))
    #This is printed: the outcome of each iteration (either screen_require_for_y or extra_screen + screen_require_for_y) on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and pairs of integers `x` and `y`. For each pair, it calculates the number of elements required based on specific conditions involving `x` and `y`. If certain conditions are met, it appends either `y // 2` or `extra_screen + y // 2` to a list. Finally, it prints each element in the list on a new line.

