#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: result is a list of integers representing the number of screens required for each pair of x and y processed in the loop.
    print('\n'.join(map(str, result)))
    #This is printed: Each integer from the `result` list printed on a new line (where `result` is a list of integers representing the number of screens required for each pair of x and y processed in the loop)
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `x` and `y`. For each test case, it calculates the number of screens required based on the given conditions and outputs the result for each test case on a new line.

