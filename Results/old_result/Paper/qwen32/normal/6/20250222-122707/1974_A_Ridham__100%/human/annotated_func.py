#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99) where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
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
        
    #State: `n` is 0, `result` is a list of integers representing the number of screens required for each test case, `x` and `y` are the values of the last test case, `space_x` is `x` from the last test case, `space_y` is `y * 4` from the last test case, `total_space` is `space_x + space_y` from the last test case, `screen_require_for_y` is the number of screens required for `y` in the last test case, `remaining_cells` is the remaining cells on the screens for `y` in the last test case, `extra_space` and `extra_screen` are the additional space and screens required for `x` in the last test case if `x` did not fit within the remaining cells.
    print('\n'.join(map(str, result)))
    #This is printed: (an empty string)
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers representing the number of 1x1 and 2x2 applications. It calculates and prints the minimum number of screens required to accommodate all applications for each test case.

