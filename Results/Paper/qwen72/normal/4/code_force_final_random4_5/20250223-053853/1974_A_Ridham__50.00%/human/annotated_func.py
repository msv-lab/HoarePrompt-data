#State of the program right berfore the function call: The function should accept two parameters, x and y, where x and y are non-negative integers such that 0 <= x, y <= 99, representing the number of 1x1 and 2x2 icons, respectively.
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
        
    #State: The `result` list contains the number of screens required for each iteration of the loop, where the number of screens is calculated based on the values of `x` and `y` provided in the input. The length of the `result` list will be equal to `n`, the number of iterations. The variables `x` and `y` will have the values of the last input provided, and `space_x`, `space_y`, `total_space`, `screen_require_for_y`, and `remaining_cells` will be calculated based on the last values of `x` and `y`.
    print('\n'.join(map(str, result)))
    #This is printed: [result[0]]
    #[result[1]]
    #...
    #[result[n-1]] (where each [result[i]] is the number of screens required for the i-th iteration of the loop)
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads two non-negative integers `x` and `y` from the user, representing the number of 1x1 and 2x2 icons, respectively. It calculates the minimum number of 15x15 screens required to fit all the icons for each test case and appends this number to a list `result`. After processing all test cases, it prints each element of `result` on a new line, showing the number of screens required for each test case. The function does not return any value.

