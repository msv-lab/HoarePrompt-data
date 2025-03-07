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
        
    #State: Output State: The final state of the loop will depend on the value of `n`, the number of iterations the loop runs. After all iterations, `result` will be a list containing the values calculated for each iteration according to the logic inside the loop. For each iteration, `x` and `y` are read from input, and based on the conditions provided, `screen_require_for_y` and possibly `extra_screen` are calculated. These values are then appended to `result`.
    #
    #If `space_x` (which is initially `x`) is less than or equal to `remaining_cells` (calculated as `15 * screen_require_for_y - space_y`), `screen_require_for_y` is appended to `result`. Otherwise, `extra_screen` is calculated and added to `screen_require_for_y`, and the sum is appended to `result`.
    #
    #The final `result` will be a list of integers, each representing the calculated value for each iteration of the loop. The exact contents of `result` will vary based on the inputs provided during each iteration.
    print('\n'.join(map(str, result)))
    #This is printed: a list of integers, each representing the calculated value for each iteration of the loop, with each value on a new line
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(x\) and \(y\) (where \(0 \leq x, y \leq 99\)). For each test case, it calculates a value based on the given conditions and appends it to a list. Finally, it prints each value in the list on a new line. The function does not return any value but modifies and prints a list of integers derived from the input values.

