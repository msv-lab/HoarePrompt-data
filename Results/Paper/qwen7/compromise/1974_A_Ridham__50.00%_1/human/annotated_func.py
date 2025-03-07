#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `result` is a list containing integers calculated based on the conditions inside the loop for each iteration of `n`.
    print('\n'.join(map(str, result)))
    #This is printed: a string with each line representing an element from the `result` list, converted to a string and separated by newlines
#Overall this is what the function does:The function processes multiple test cases, each consisting of two non-negative integers \(x\) and \(y\), and calculates a result based on specific conditions. It then prints the results for all test cases, one per line. If \(y\) is even, it calculates half of \(y\); if odd, it calculates half of \(y\) plus one. It also considers the space requirements for \(x\) and adjusts the result accordingly. The final output is a list of integers, each representing the calculated result for a given test case.

