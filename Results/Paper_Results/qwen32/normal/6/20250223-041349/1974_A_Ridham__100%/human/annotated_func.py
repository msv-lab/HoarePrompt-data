#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
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
        
    #State: the `result` list after processing all `n` test cases.
    print('\n'.join(map(str, result)))
    #This is printed: Each element of the `result` list, each on a new line (where `result` is the list containing the outcomes of processing all `n` test cases)
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers representing the number of 1x1 and 2x2 application icons. It calculates and returns the minimum number of screens required to accommodate all the icons for each test case.

