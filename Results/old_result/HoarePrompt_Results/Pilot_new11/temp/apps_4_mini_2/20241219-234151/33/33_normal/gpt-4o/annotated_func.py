#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50; each t_i is an integer such that 1 ≤ t_i ≤ 10^6 and dir_i is a string that is either "North", "South", "West", or "East".
def func():
    n = int(input())
    position = 0
    valid = True
    for _ in range(n):
        t, dir = input().split()
        
        t = int(t)
        
        if dir == 'North':
            if position - t < 0:
                valid = False
            position -= t
        elif dir == 'South':
            if position + t > 20000:
                valid = False
            position += t
        elif dir in ('West', 'East'):
            if position == 0 or position == 20000:
                valid = False
        
        if position < 0 or position > 20000:
            valid = False
        
    #State of the program after the  for loop has been executed: `position` is the final position after all steps, `valid` indicates if the moves were all within permitted limits, `n` remains the initial input integer between 1 and 50, `t_i` and `dir_i` are the inputs received during the iterations, and if any invalidation conditions were met, `valid` will be `False`.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`position` is the final position after all steps and is not equal to 0, `valid` is False, `n` remains the initial input integer between 1 and 50, and `t_i` and `dir_i` are the inputs received during the iterations.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`position` is the final position after all steps and is not equal to 0, `n` remains the initial input integer between 1 and 50, and `t_i` and `dir_i` are the inputs received during the iterations. If `valid` is True, 'YES' is printed. If `valid` is False, no 'YES' is printed.
#Overall this is what the function does:The function processes a series of directional movements based on user input and checks if the movements are valid according to specific constraints. It does not accept parameters, and it takes an integer input `n` (the number of movements) followed by `n` lines of input containing an integer `t` (the distance) and a string `dir` (the direction). The function maintains a `position` variable that reflects the user's current position, initialized to 0, and a boolean `valid` to track the validity of the movements. If any movement attempts to go below 0 or above 20000, or if specific direction constraints are violated (e.g., attempting to move 'West' or 'East' when at the limits), the `valid` flag is set to False. Following all movements, the function evaluates whether the final position is 0, and if all movements were valid. If `valid` is True and the final position is 0, it prints 'YES'; otherwise, it prints 'NO'. The function may miss a check to invalidate movements to 'West' or 'East' by not updating the `valid` flag accordingly after those direction attempts, leading to potential unforeseen outcomes. Overall, it evaluates the movement logic within the constraints of the problem and provides a simple verification based on these rules.

