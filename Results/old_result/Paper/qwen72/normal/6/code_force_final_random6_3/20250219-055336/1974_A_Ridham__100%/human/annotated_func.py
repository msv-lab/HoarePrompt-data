#State of the program right berfore the function call: The function should take two parameters, x and y, where x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: `x` and `y` are integers provided by the user, `n` is 0, `result` is a list containing the number of screens required for each pair of `x` and `y` values entered. For each pair, if `y` is even, the number of screens required is `y // 2`. If `y` is odd, the number of screens required is `y // 2 + 1`. If `space_x` (which is `x * 1`) is less than or equal to the remaining cells (calculated as `15 * screen_require_for_y - y * 4`), then the number of screens required for that pair is `screen_require_for_y`. Otherwise, the number of screens required is `extra_screen + screen_require_for_y`, where `extra_space` is `x * 1 - (15 * screen_require_for_y - y * 4)`, and `extra_screen` is `extra_space // 15` if `extra_space % 15 == 0`, or `extra_space // 15 + 1` if `extra_space % 15 != 0`.
    print('\n'.join(map(str, result)))
    #This is printed: [number of screens required for each pair of x and y values, each on a new line]
#Overall this is what the function does:The function `func` reads an integer `n` from the user, which represents the number of pairs of integers `(x, y)` to process. For each pair `(x, y)`, it calculates the number of screens required based on the space occupied by `x` and `y`. The space occupied by `y` is `y * 4`, and the space occupied by `x` is `x * 1`. If `y` is even, the number of screens required for `y` is `y // 2`; if `y` is odd, it is `y // 2 + 1`. The function then checks if the space occupied by `x` fits into the remaining cells on the screens allocated for `y`. If it does, the total number of screens required is the number of screens for `y`. If it doesn't, the function calculates the additional screens needed for the remaining `x` space and adds this to the total. The function prints the number of screens required for each pair `(x, y)` on a new line.

