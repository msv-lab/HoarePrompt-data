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
        
    #State: result is a list of integers where each integer represents the number of screens required for each test case.
    print('\n'.join(map(str, result)))
    #This is printed: The `print` statement will output each integer from the `result` list on a new line.
    #
    #Output:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y` and calculates the number of screens required based on the given conditions. It then outputs the number of screens required for each test case on a new line.

