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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `result` is a list containing integers calculated based on the conditions inside the loop for each iteration of `n`.
    print('\n'.join(map(str, result)))
    #This is printed: a series of integers, each on a new line, derived from the loop conditions based on `n`
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer \( t \) (where \( 1 \leq t \leq 10^4 \)). For each test case, it reads pairs of integers \( x \) and \( y \) (where \( 0 \leq x, y \leq 99 \)), calculates the required screen space based on certain conditions, and appends the result to a list. After processing all test cases, it prints the results, one per line.

