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
            if extra_space % 15 == 0:
                extra_screen = extra_space // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: `result` is a list containing the number of screens required for each test case based on the given conditions. The length of `result` is equal to `n`, and each element in `result` represents the total number of screens required for the corresponding test case. The values of `t`, `x`, `y`, and `n` remain unchanged.
    print('\n'.join(map(str, result)))
    #This is printed: [result[0]]
    #[result[1]]
    #...
    #[result[n-1]] (where each [result[i]] is the number of screens required for the corresponding test case)
#Overall this is what the function does:The function `func` reads an integer `n` indicating the number of test cases. For each test case, it reads two integers `x` and `y` (0 <= x, y <= 99). It calculates the number of screens required based on the space needed for `x` and `y` and appends the result to a list `result`. After processing all test cases, it prints each element of `result` on a new line, where each element represents the total number of screens required for the corresponding test case. The function does not return any value, but the state of the program after the function concludes includes a printed list of screen requirements for each test case, and the values of `t`, `x`, `y`, and `n` remain unchanged.

