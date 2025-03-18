#State of the program right berfore the function call: The function `func` is expected to take two parameters, `x` and `y`, where `x` and `y` are integers such that 0 <= x, y <= 99.
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
        
    #State: `n` is the same input integer, `x` and `y` are the last input integers such that 0 <= x, y <= 99, `result` is a list containing the number of screens required for each iteration.
    print('\n'.join(map(str, result)))
    #This is printed: [result[0]]
    #[result[1]]
    #...
    #[result[len(result) - 1]] (where each element of `result` is an integer representing the number of screens required for each iteration)
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of iterations. For each iteration, it reads two integers `x` and `y` from the input, where both `x` and `y` are in the range 0 to 99, inclusive. It calculates the number of screens required based on the values of `x` and `y`, and appends this number to a list `result`. After all iterations, the function prints each element of `result` on a new line, where each element represents the number of screens required for the corresponding iteration. The function does not return any value.

