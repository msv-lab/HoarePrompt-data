#State of the program right berfore the function call: The function `func` is supposed to take two integers `x` and `y` as input, where 0 <= x, y <= 99, representing the number of applications with a 1 x 1 icon and the number of applications with a 2 x 2 icon, respectively. However, the function definition provided does not include these parameters. The correct function definition should be `def func(x, y):`.
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
        
    #State: The `result` list will contain the calculated number of screens required for each iteration, based on the input values of `x` and `y`. The length of the `result` list will be equal to `n`, and each element in the list will be an integer representing the total number of screens required for the corresponding `x` and `y` values. The values of `x` and `y` will be updated for each iteration but are not retained after the loop.
    print('\n'.join(map(str, result)))
    #This is printed: [result[0]]
    #[result[1]]
    #...
    #[result[n-1]] (where each [result[i]] is an integer representing the number of screens required for the corresponding iteration)
#Overall this is what the function does:The function `func` reads an integer `n` from the user, representing the number of test cases. For each test case, it reads two integers `x` and `y` from the user, where `x` is the number of applications with a 1 x 1 icon and `y` is the number of applications with a 2 x 2 icon. It calculates the total number of screens required to fit all the icons, considering that each screen can hold up to 15 cells (1 x 1 icons) and 2 x 2 icons take up 4 cells each. The function then prints the number of screens required for each test case, one per line. The function does not return any value.

