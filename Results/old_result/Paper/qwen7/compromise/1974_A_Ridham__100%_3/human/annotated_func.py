#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `result` is a list containing integers calculated based on the input values of `x` and `y` for each iteration of the loop.
    print('\n'.join(map(str, result)))
    #This is printed: a series of integers, each on a new line, from the `result` list
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(x\) and \(y\). For each test case, it calculates the number of screens required based on the values of \(x\) and \(y\), considering certain conditions. The function then prints these calculated numbers of screens, one per line, for all test cases.

