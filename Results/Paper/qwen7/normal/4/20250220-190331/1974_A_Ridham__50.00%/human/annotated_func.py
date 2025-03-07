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
        
    #State: Output State: The output state after the loop executes all iterations is as follows: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is the total number of iterations the loop has executed, `result` is a list containing the final values computed for each iteration based on the conditions within the loop. Each element in `result` is either `screen_require_for_y` or `extra_screen + screen_require_for_y`, where `screen_require_for_y` is calculated as `y // 2 + 1` if `y` is even, or `y // 2` if `y` is odd, and `extra_screen` is determined by the remaining cells and `space_x`. `x` is the first integer entered for each iteration, `y` is the second integer entered for each iteration, `space_x` is equal to `x`, `space_y` is equal to `y * 4`, `total_space` is equal to `space_y + space_x`, and `remaining_cells` is calculated as `15 * screen_require_for_y - space_y` if `y` is even, or `15 * (y // 2 + 1) - space_y` if `y` is odd. The final state of `result` will contain the sum of `screen_require_for_y` or `extra_screen + screen_require_for_y` for each iteration of the loop.
    print('\n'.join(map(str, result)))
    #This is printed: the elements of the `result` list, each on a new line
#Overall this is what the function does:The function reads a series of test cases, each containing two integers \(x\) and \(y\). For each test case, it calculates the number of screens required based on specific conditions involving \(x\) and \(y\). If \(y\) is even, the number of screens required is \(y // 2\); if \(y\) is odd, it is \(y // 2 + 1\). It then checks if the available space (\(space_x\)) is sufficient; if not, it calculates the additional screens needed. The function compiles these results into a list and prints each result on a new line.

