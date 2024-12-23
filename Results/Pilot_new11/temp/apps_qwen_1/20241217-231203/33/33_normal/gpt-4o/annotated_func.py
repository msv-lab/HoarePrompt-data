#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50. For each i where 1 ≤ i ≤ n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6 and dir_{i} is a string representing a direction ("North", "South", "West", "East").
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
        
    #State of the program after the  for loop has been executed: `position` is an integer between 0 and 20000 (inclusive), `dir` is a string representing a direction ("North", "South", "West", "East"), `n` is 0, `valid` is False, and `t` is an integer. If `valid` is False, all other variables retain their final values from the last iteration of the loop; otherwise, `n` becomes 0 and `valid` remains False.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`position` is an integer between 0 and 20000 (inclusive), `dir` is a string representing a direction ("North", "South", "West", "East"), `n` is 0, `valid` is False, and `t` is an integer; if `position` is not 0, `valid` is set to False. Otherwise, the values of all variables remain unchanged.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`position` is an integer between 0 and 20000 (inclusive), `dir` is a string representing a direction ("North", "South", "West", "East"), `n` is 0, `valid` is either True or False based on the condition `position != 0`, and `t` is an integer. If `position` is not 0, `valid` is set to False, and if `position` is 0, the function prints 'NO' and does not change the value of `valid`.
#Overall this is what the function does:The function processes a series of movements in a 20000-unit long corridor, starting from a position of 0. It reads `n` movements where each movement consists of a distance `t` and a direction (`North`, `South`, `West`, `East`). The function checks if each movement is within valid limits and updates the position accordingly. If any movement causes the position to go out of bounds (less than 0 or greater than 20000), or if the position ends up not being 0 after all movements, the function sets the `valid` flag to `False`. If the `valid` flag remains `True` after processing all movements and the final position is 0, the function prints 'YES'; otherwise, it prints 'NO'. Potential edge cases include positions going out of bounds during any movement, and the final position not being 0.

