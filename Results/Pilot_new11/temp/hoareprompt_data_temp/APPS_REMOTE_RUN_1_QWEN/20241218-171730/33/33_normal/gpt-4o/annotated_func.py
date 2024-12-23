#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50. For each i in range 1 to n, t_{i} is an integer such that 1 ≤ t_{i} ≤ 10^6, and dir_{i} is a string representing the direction of movement which can be one of "North", "South", "West", or "East".
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 50 (inclusive), `t_i` is an integer such that 1 ≤ `t_i` ≤ 10^6 for each i in range 1 to `n`, `dir_i` is a string representing the direction of movement which can be one of "North", "South", "West", or "East" for each i in range 1 to `n`, `position` is a non-negative integer within the range [0, 20000] or 0 if the loop did not execute, and `valid` is `True` if the loop did not terminate due to invalid movements, otherwise `valid` is `False`.
    if (position != 0) :
        valid = False
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 50 (inclusive), `t_i` is an integer such that 1 ≤ `t_i` ≤ 10^6 for each i in range 1 to `n`, `dir_i` is a string representing the direction of movement which can be one of "North", "South", "West", or "East" for each i in range 1 to `n`, `position` is a non-negative integer within the range [0, 20000], `valid` is `False` since the condition `position != 0` is met and the if part of the if-else block is executed.
    if valid :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 50 (inclusive), `t_i` is an integer such that 1 ≤ `t_i` ≤ 10^6 for each i in range 1 to `n`, `dir_i` is a string representing the direction of movement which can be one of "North", "South", "West", or "East" for each i in range 1 to `n`, `position` is a non-negative integer within the range [0, 20000], `valid` is `True` since the condition `position != 0` is met, and the console prints 'YES' if the if part is executed, otherwise it prints 'NO'.
#Overall this is what the function does:The function processes a series of movements defined by an integer `n` and corresponding directions and distances. It checks if each movement is valid based on the position constraints and direction restrictions. After processing all movements, it determines if the final position is 0. If the final position is 0, the function prints 'YES', indicating that all movements were valid and the final position is 0. Otherwise, it prints 'NO', indicating that the final position is not 0 or that any of the movements were invalid. Potential edge cases include movements that would cause the position to go out of bounds (less than 0 or greater than 20000) or invalid directions (only "North", "South", "West", or "East" are allowed). The function also checks if the initial or final position is exactly 0, which would make the movement invalid.

