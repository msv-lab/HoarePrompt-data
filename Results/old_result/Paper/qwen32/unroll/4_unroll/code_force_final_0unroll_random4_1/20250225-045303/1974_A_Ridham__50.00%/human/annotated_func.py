#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives two integers x and y (0 ≤ x, y ≤ 99), where x is the number of applications with a 1 × 1 icon and y is the number of applications with a 2 × 2 icon.
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
        
    #State: The `result` list contains the number of screens required for each test case after processing all `n` test cases. Each entry in `result` is calculated based on the number of 1x1 and 2x2 application icons provided in the input for that specific test case. The other variables (`t`, `x`, `y`, `space_x`, `space_y`, `total_space`, `screen_require_for_y`, `remaining_cells`, `extra_space`, and `extra_screen`) do not retain their values after the loop execution and are used only within the scope of each iteration.
    print('\n'.join(map(str, result)))
    #This is printed: Each line contains the number of screens required for each test case (where each number in the result list corresponds to the number of screens needed for each respective test case)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a specified number of 1x1 and 2x2 application icons. For each test case, it calculates and outputs the minimum number of screens required to accommodate all the icons, assuming each screen can hold up to 15 cells.

