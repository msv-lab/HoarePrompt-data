#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, x and y are integers such that 0 <= x, y <= 99.
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
        
    #State: `result` is a list containing the number of screens required for each test case, based on the calculations performed within the loop. The length of `result` is equal to `n`, and each element in `result` corresponds to the number of screens required for the respective test case.
    print('\n'.join(map(str, result)))
    #This is printed: [result[0]]
    #[result[1]]
    #...
    #[result[n-1]] (where each element is the number of screens required for the respective test case)
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of two integers `x` and `y` (where 0 <= x, y <= 99). For each test case, it calculates the number of screens required based on the space occupied by `x` and `y` and the available space on the screens. The function then prints the number of screens required for each test case, one per line. The final state of the program is that the `result` list contains the number of screens required for each test case, and these values are printed to the console.

