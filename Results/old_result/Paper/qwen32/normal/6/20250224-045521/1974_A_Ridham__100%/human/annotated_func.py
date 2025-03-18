#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers x and y (0 ≤ x, y ≤ 99) where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
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
        
    #State: result is a list containing the number of screens required for each of the t test cases, n is 0, and x and y are the values from the last test case.
    print('\n'.join(map(str, result)))
    #This is printed: Each element of the `result` list printed on a new line (where `result` is a list of integers representing the number of screens required for each test case)
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `x` and `y`, where `x` is the number of applications with a 1 × 1 icon and `y` is the number of applications with a 2 × 2 icon. It calculates and prints the minimum number of screens required to accommodate all applications for each test case.

