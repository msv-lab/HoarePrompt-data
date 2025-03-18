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
        
    #State: Output State: The loop has executed all its iterations, meaning `n` has been reduced to 0. At this point, `t` remains an integer such that 1 ≤ t ≤ 10^4, and `n` is 0. The `result` list contains all the elements added during each iteration of the loop, which can be either `screen_require_for_y` or `extra_screen + screen_require_for_y` depending on the conditions met during each iteration. `space_x` and `space_y` are updated according to the last iteration's input values `x` and `y`, and `total_space` is the sum of `space_y` and `space_x`. `screen_require_for_y` is calculated as `y // 2` if `y` is even, or `y // 2 + 1` if `y` is odd, and `extra_screen` is determined based on whether `space_x` is divisible by 15 or not.
    #
    #In summary, the final `result` list will contain up to `n` elements, each either `screen_require_for_y` or `extra_screen + screen_require_for_y`, with `t` and `n` adjusted accordingly, and `space_x`, `space_y`, `total_space`, `screen_require_for_y`, and `extra_screen` reflecting the last iteration's input values.
    print('\n'.join(map(str, result)))
    #This is printed: \n'.join(map(str, result)) (where result is a list containing elements that are either screen_require_for_y or extra_screen + screen_require_for_y, with screen_require_for_y calculated as y // 2 if y is even, or y // 2 + 1 if y is odd, and extra_screen determined based on whether space_x is divisible by 15 or not)
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of two integers \(x\) and \(y\). For each test case, it calculates the number of screens required based on certain conditions involving \(x\) and \(y\), and appends the result to a list. Finally, it prints the elements of the list, each representing the number of screens required for the respective test case.

