#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    i = 1
    while i <= 1000:
        x = randint(1, 9)
        
        y = randint(1, 9)
        
        z = randint(1, 9)
        
        res = ''
        
        if x < y:
            if y > z:
                res = 'peak'
            elif y < z:
                res = 'stair'
            else:
                res = 'none'
        else:
            res = 'none'
        
        print(x, y, z, sep=' ')
        
        print(res)
        
        i += 1
        
    #State: Output State: The output state will consist of 1000 lines, each containing four elements: three integers between 1 and 9 (inclusive) representing `x`, `y`, and `z`, and a string ('peak', 'stair', or 'none') representing the result of the conditional checks.
    #
    #Each line will be formatted as follows:
    #- The first integer (`x`) will be compared with the second integer (`y`).
    #- If `x` is less than `y`, then `y` will be compared with `z`.
    #  - If `y` is greater than `z`, the result will be 'peak'.
    #  - If `y` is less than `z`, the result will be 'stair'.
    #  - If `y` equals `z`, the result will be 'none'.
    #- If `x` is not less than `y`, the result will always be 'none'.
    #
    #The loop will iterate from `i = 1` to `i = 1000`, generating new random values for `x`, `y`, and `z` on each iteration.
#Overall this is what the function does:The function generates and prints 1000 lines of output. Each line contains three random integers between 1 and 9 (inclusive) and a string ('peak', 'stair', or 'none'). The string is determined based on the comparison of these integers: if the first integer is less than the second and the second is greater than the third, the result is 'peak'; if the first is less than the second and the second is less than the third, the result is 'stair'; otherwise, the result is 'none'. The function does not return any value.

