#State of the program right berfore the function call: The function takes no arguments. The input is read from standard input and consists of t (1 ≤ t ≤ 10^4) test cases. Each test case contains two integers x and y (0 ≤ x, y ≤ 99) representing the number of 1x1 and 2x2 application icons, respectively.
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
        
    #State: `result` is a list containing the calculated number of screens required for each test case based on the given conditions.
    print('\n'.join(map(str, result)))
    #This is printed: Each element of the `result` list printed on a new line (where each element is the number of screens required for a test case)
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers representing the number of 1x1 and 2x2 application icons. It calculates the minimum number of 5x3 screens required to fit all the icons for each test case and prints the results, one per line.

